from scrapybara import Scrapybara
from dotenv import load_dotenv
import os

load_dotenv()

client = Scrapybara(
    api_key=os.getenv("SCRAPYBARA_API_KEY", "YOUR_API_KEY"),
    timeout=600,
)

# 1. Start instance
instance = client.start(instance_type="large")

# 2. Scrape W25 companies
response = instance.agent.scrape(
    cmd="Go to https://ycombinator.com/companies, set batch filter to W25, and scrape all W25 companies.",
    schema={
        "companies": [
            {
                "name": "str",
                "description": "str",
                "tags": "str[]",
            }
        ]
    },
)
print(f"Scraped W25 companies: {response.data['companies']}")

COMPANY_LIMIT = 3

# 3. Find best way to contact each company
for company in response.data["companies"][0:COMPANY_LIMIT]:
    print(f"\nFinding contact info for {company['name']}...")
    contact_info = instance.agent.scrape(
        cmd=f"Go to https://ycombinator.com/companies and find the best way to contact YC W25 company {company['name']} - {company['description']}. Try their website, LinkedIn, and Twitter/X.",
        schema={
            "contact_method": "str",
            "contact_details": "str",
        },
    )
    print(f"\nFound contact info for {company['name']}: {contact_info.data}")


# 4. Draft messages for every company
instance.agent.act(
    cmd=f"Open LibreOffice, draft a two sentence message to each of the following YC W25 companies, advertising a capybara zoo in Japan: {response.data['companies'][0:COMPANY_LIMIT]}"
)
print("\nDrafted messages")

# 5. Stop instance
instance.stop()

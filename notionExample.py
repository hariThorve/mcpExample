from notion_client import Client
from datetime import datetime, timedelta

def add_todo_record(
    notion_token: str,
    database_id: str,
    name: str,
    priority: str,
    due_date: str,
    todo_description: str,
    completion: bool = False
):
    notion = Client(auth=notion_token)
    response = notion.pages.create(
        parent={"database_id": database_id},
        properties={
            "Name": {
                "title": [
                    {
                        "text": {
                            "content": name
                        }
                    }
                ]
            },
            "priority": {
                "select": {
                    "name": priority
                }
            },
            "due date": {
                "date": {
                    "start": due_date
                }
            },
            "name of the to-do": {
                "rich_text": [
                    {
                        "text": {
                            "content": todo_description
                        }
                    }
                ]
            },
            "completion": {
                "checkbox": completion
            }
        }
    )
    return response

# Example usage:
if __name__ == "__main__":
    NOTION_TOKEN = "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"  # Replace with your integration token
    DATABASE_ID = "1e3e1d1f-35be-81db-aead-d9f3ca5c4b44"  # Use hyphenated format

    # Set due date to one week from today
    due_date = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")

    add_todo_record(
        notion_token=NOTION_TOKEN,
        database_id=DATABASE_ID,
        name="Complete CNN Project",
        priority="High",
        due_date=due_date,
        todo_description="I have to complete my cnn project",
        completion=False
    )
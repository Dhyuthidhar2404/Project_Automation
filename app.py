from flask import Flask, render_template, request
from github import Github
from flask_ckeditor import CKEditor
import base64
import datetime
import json
import requests
import re

app = Flask(__name__, static_url_path='/static')
ckeditor = CKEditor(app)

GITHUB_REPO_OWNER = 'Dhyuthidhar2404'
GITHUB_REPO_NAME = 'personal_blog'
GITHUB_API_TOKEN = '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'
HASHNODE_API_KEY = 'cf8158bd-935d-4236-bfd9-80cb4c5aa272'
publication_id = "6328962199624fc71cd522e1"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post_article', methods=['POST'])
def post_article():
    title = request.form['title']
    content = request.form['content']
    cover_image_url = request.form['cover_image_url']
    tags = [tag.strip() for tag in request.form['tags'].split(',')] # Split tags by comma and space
    # Post to Hashnode
    hashnode_response = post_to_hashnode(title, content, publication_id, HASHNODE_API_KEY, cover_image_url, tags)

    # Post to GitHub
    github_response = post_to_github(title, content)

    return render_template('result.html', hashnode_response=hashnode_response, github_response=github_response)

def generate_slug(title):
    # Remove non-alphanumeric characters and replace spaces with hyphens
    slug = re.sub(r'[^a-zA-Z0-9\s]', '', title).replace(' ', '-').lower()

    # Ensure the slug matches the required pattern
    # Corrected regular expression to retain valid characters
    slug = re.sub(r'^(badges|newsletter|sponsor|archive|members)$', '', slug)

    # Set a default slug if the generated one is empty
    return slug or "Programming"  # Ensure the default slug also conforms to Hashnode's pattern


def post_to_hashnode(title, content, publication_id, api_key, cover_image_url, tags):
    url = 'https://gql.hashnode.com/'

    # Generate the published_at value
    published_at = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    query = '''
        mutation PublishPost($input: PublishPostInput!) {
          publishPost(input: $input) {
            post {
              id
              publishedAt
              slug
              tags {
                name
              }
              title
              url
            }
          }
        }
    '''

    input_variables = {
        "input": {
            "publicationId": publication_id,
            "title": title,
            "contentMarkdown": content,
            "publishedAt": published_at,
            'coverImageOptions': {
                'coverImageURL': cover_image_url
            },
            "slug": generate_slug(title),
            "tags": [{"slug": tag.lower(), "name": tag} for tag in tags],
            "disableComments": False,
            "metaTags": {
                "title": title,
                "description": "Learn Types of ML models.",
                "image": "https://cdn.hashnode.com/res/hashnode/image/upload/v1703324455858/1750cab8-1b98-4248-a398-efb14de437af.png"
            },
            "settings": {
                "scheduled": False,
                "enableTableOfContent": False,
                "slugOverridden": True,
                "isNewsletterActivated": False,
                "delisted": False
            }
        }
    }

    headers = {
        'Content-Type': 'application/json',
        'Authorization': api_key,
    }

    response = requests.post(url, json={"query": query, "variables": input_variables}, headers=headers)
    response_body = response.json()

    if response_body.get('errors') and len(response_body['errors']) > 0:
        raise ValueError(', '.join([e['message'] for e in response_body['errors']]))

    return response_body

def post_to_github(title, content):
    g = Github(GITHUB_API_TOKEN)
    user = g.get_user()
    repo = user.get_repo(GITHUB_REPO_NAME)
    file_path = f'personal_blog/{title.replace(" ", "_")}.md'

    # Check if the file exists to retrieve the current SHA
    file_exists = True
    try:
        existing_file = repo.get_contents(file_path)
        current_sha = existing_file.sha
    except Exception as e:
        # Handle the case where the file does not exist yet
        current_sha = None
        file_exists = False

    # Specify the new content
    file_content = f"---\ntitle: {title}\ndate: {datetime.datetime.utcnow().isoformat()}\n---\n\n{content}"

    # Specify the commit message
    commit_message = f"Add {title} article"

    # Create or update the file with the new content and SHA (if it exists)
    if file_exists:
        repo.update_file(file_path, commit_message, file_content, current_sha, branch="main")
    else:
        repo.create_file(file_path, commit_message, file_content, branch="main")

    return {"status": "Success", "message": f"Article '{title}' posted to GitHub."}

if __name__ == '__main__':
    app.run(debug=True)

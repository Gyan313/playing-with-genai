from llamaapi import LlamaAPI
import streamlit as st
from dotenv import load_dotenv
import json
import os

load_dotenv()

llama = LlamaAPI(os.getenv('LLAMA_API_KEY'))

api_request_json = {
  "model": "llama3-70b",
  "messages": [
    {"role": "system", "content": "Estimate an approximate time till we reach mars?"},
    {"role": "user", "content": "Hi, happy llama day!"},
  ]
}

response = llama.run(api_request_json)
print(json.dumps(response.json(), indent=2))
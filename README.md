# **Facebook Post and Comments Scraper**

This Python script allows you to retrieve information from a Facebook post and its comments, and store it in a file protected by a hash.

## **Prerequisites**

- Facebook API key
- Python 3.x
- **`facebook-sdk`** module

## **Usage**

1. Replace **`inserisci_qui_la_tua_api_key`** with your Facebook API key.
2. Run the script in a Python environment.
3. Follow the prompts to input the user ID and post ID.
4. Follow the prompts to input the comment ID you want to retrieve.
5. The script will output the post and comment information to the console.
6. A file named **`lista_commenti.txt`** will be created with the post and comment information.
7. A file named **`hash.txt`** will be created with the hash of the **`lista_commenti.txt`** file.

## **Notes**

- This script uses the **`md5`** hashing algorithm to protect the contents of the file.
- The script reads the file in blocks of 64 KB to prevent memory issues when working with large files.
- This script is for educational purposes only and should not be used to violate Facebook's policies or infringe on the privacy of others.

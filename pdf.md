

# GitHub Command-Line Cheat Sheet

A quick reference guide for adding code to a GitHub repository from your terminal. This covers two main workflows: the pure command-line method and the hybrid method using the GitHub website.

-----

## Workflow 1: The Pure Command-Line Method (Recommended)

This workflow uses `git` and the **GitHub CLI (`gh`)** to do everything from your terminal without ever opening the GitHub website. It's fast, efficient, and scriptable.

### ➤ Step 1: One-Time Setup (Install & Authenticate `gh`)

You only need to do this once per machine.

1.  **Install GitHub CLI (`gh`)**:

      * **Windows (winget)**: `winget install --id GitHub.cli`
      * **macOS (brew)**: `brew install gh`
      * **Linux (apt)**: `sudo apt install gh`

2.  **Log in to your GitHub account**:

    ```bash
    gh auth login
    ```

      * Follow the on-screen prompts. Choose **HTTPS** as your preferred protocol and log in using a web browser.

### ➤ Step 2: Create a New Project & Push for the First Time

Use this when you have a code folder locally that you want to put on GitHub.

1.  **Navigate to your project directory**:

    ```bash
    cd path/to/your/project
    ```

2.  **Initialize a Git repository**:

    ```bash
    git init
    ```

3.  **Stage and commit your files**:

    ```bash
    # Stage all files in the current directory
    git add .

    # Save a snapshot of the changes
    git commit -m "Initial commit"
    ```

4.  **Create the repository on GitHub and push your code**:

    ```bash
    # This command will guide you interactively
    gh repo create
    ```

      * It will ask you to confirm the repository name, description, visibility (Public/Private), and finally, it will set up the remote connection and push your code for you.

### ➤ Step 3: Daily Workflow (Updating an Existing Project)

After the initial setup, you'll follow this simple process every day.

1.  **Check the status of your changes** (good practice):

    ```bash
    git status
    ```

2.  **Stage your changes**:

    ```bash
    # Stage all new and modified files
    git add .
    ```

3.  **Commit your changes with a descriptive message**:

    ```bash
    git commit -m "Feat: Add new user profile page"
    ```

4.  **Push your commits to GitHub**:

    ```bash
    git push
    ```

-----

## Workflow 2: The Hybrid Method (Website + Terminal)

This workflow involves creating the repository on the GitHub website first and then using `git` in the terminal to push your code to it.

### ➤ Step 1: Create a New Repository on GitHub.com

1.  Log in to [GitHub.com](https://github.com).
2.  Click the **`+`** icon in the top right and select **New repository**.
3.  Fill in the repository name.
4.  **Important**: Leave the options to add a README, .gitignore, or license **unchecked**.
5.  Click **Create repository**.
6.  On the next page, copy the repository URL. It will look like this: `https://github.com/your-username/your-repo-name.git`.

### ➤ Step 2: Push Your Local Code for the First Time

Now, go to your terminal.

1.  **Navigate to your project directory**:

    ```bash
    cd path/to/your/project
    ```

2.  **Initialize a Git repository**:

    ```bash
    git init
    ```

3.  **Stage and commit your files**:

    ```bash
    git add .
    git commit -m "Initial commit"
    ```

4.  **Connect your local repo to the one on GitHub**:

    ```bash
    # Replace the URL with the one you copied from GitHub
    git remote add origin https://github.com/your-username/your-repo-name.git
    ```

5.  **Push your code to GitHub**:

    ```bash
    # The -u flag sets the upstream link for future pushes
    git push -u origin main
    ```

### ➤ Step 3: Daily Workflow (Updating an Existing Project)

This is identical to the pure CLI method.

1.  **Stage changes**: `git add .`
2.  **Commit changes**: `git commit -m "Your descriptive message"`
3.  **Push changes**: `git push`

-----

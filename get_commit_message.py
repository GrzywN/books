from git import Repo
from pyperclip import copy

if __name__ == "__main__":
    repo = Repo(".", search_parent_directories=True)
    git_dir = repo.git.rev_parse("--show-toplevel")

    untracked_files = repo.untracked_files
    
    if len(untracked_files) == 0:
        print("There are no files, which are untracked.")
        exit()

    first_untracked_file = untracked_files[0]
    splited_path = first_untracked_file.split('/')

    book_name = splited_path[0]
    file_name = splited_path.pop()
    chapter_name = splited_path.pop()

    commit_name = f"{book_name}: {chapter_name}"

    print(commit_name)
    copy(commit_name)
    print('\nCopied to clipboard.')

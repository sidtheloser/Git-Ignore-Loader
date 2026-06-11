# Git Ignore Loader

This gitignore loader makes use of [TopTal's gitignore generator service](https://www.toptal.com/developers/gitignore) and falls back to [GitHub's own gitignore repository](https://github.com/github/gitignore/) when TopTal's service isn't functional.

> Builds, when?
>
> Builds for this project will be coming out soon! I need this more than you do :cry:

## Why use TopTal's gitignore service at all?

This is so we wouldn't need to ping GitHub's servers multiple times using your machine. Instead, TopTal combines all the gitignores of all the languages we desire and sends it to us in a silver platter. **The only catch is that they put their own url and comments in the gitignore compared to GitHub's repo files.**

When we try to download straight from GitHub's own repo, we need to ping their API a couple of times which could lead to your machine's IP address getting blocked by GitHub.

## Requirements

|Name|`pip` command|
|-|-|
|`requests`|`pip install requests`|
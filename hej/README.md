# Lexicon_Group_3_SMS Django project

## Run project dev environment

```bash
python manage.py runserver
```

## Git way of working

### New feature branch

Get feture branch name from Trello URL.

Stand on main run:

```bash
git checkout -b 26-add-to-readmemd
```

Update remote origin (where you push to) it kinda names the target branch on remote.

```bash
git push -u origin 26-add-to-readmemd
```

Here you can create a **PR as a draft**. As it is a nice way to see your changes while working.

Add message to all commits use the id from the trello URL like this:

```bash
git commit -m "26: I added some stuff"
```

When you are done with your feature branch change your PR to **"Ready for review"** wich will change it from a draft.

When pullrequest is ready for merge standing on your feature branch run:

```bash
git checkout main
git pull
git checkout 26-add-to-readmemd
git rebase main
```

After that make sure the project works/looks OK.

Now you are ready to merge!

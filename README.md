# GPT3 chatbot in your terminal

This is a dead simple script that will send your queries to GPT-3 and show the responses in your terminal.

## Instructions

### Install gpto

Download from [the repo](https://github.com/alanvardy/gpto) and set it up. The script calls that to query GPT-3.

### Ask a single question

```
python app.py how do i eat an egg
```

Don't include any special characters like `?`, `:`, etc that may confuse your CLI!

### Ask lots of questions

```
python app.py
```

The script will open in interactive mode and you can ask multiple questions.

Be aware that it currently doesn't remember context, so it won't be able to remember what your wrote in your prior queries. In future I'll look at retaining some context, like ChatGPT.

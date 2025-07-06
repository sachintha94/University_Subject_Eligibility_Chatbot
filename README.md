# University_Subject_Eligibility_Chatbot (Ongoing development)
A simple chatbot that helps students find out which university subjects they can take, based on prerequisites and credits. It uses data from the university guidebook to answer questions. (Still under development)

## Project Overview

My project is an AI-powered chatbot that answers student questions about university subjects, like:
- “Can I take EEX5270 if I failed EEX3336?”
- “How many credits do I need for EEX5270?”
Instead of searching PDF guidebooks, students simply ask the chatbot in natural language and get instant answers.

## NLP (Natural Language Processing)
This project uses NLP (Natural Language Processing) — a field of AI that helps computers understand and generate human language.
NLP is what lets my chatbot:
  - understand different ways students ask questions
  - generate human-like answers

This is my main NLP library.
Why Hugging Face?
  - easy access to LLMs like T5, BART, GPT-2
  - perfect for fine-tuning models on my custom Q&A data
I chose T5-small, a powerful LLM that:
  - takes a question as input
  - generates the answer as output
  - works well for Q&A tasks

### Data Preparation
I extracted data from PDFs into a CSV of Q&A pairs.
I cleaned the data by.
 - converting text to lowercase
 - removing duplicates
 - removing extra spaces

### NLP Tokenization
NLP models like T5 can’t read plain text. They need tokens (numbers) instead.

## LLM (Large Language Model)
Fine-tuning = training an LLM on my own data.
I fine-tuned T5-small on my Q&A pairs.

        from transformers import Trainer
        
        trainer = Trainer(
            model=model,
            args=training_args,
            train_dataset=tokenized_dataset,
            data_collator=data_collator
        )
        
        trainer.train()

Building this chatbot helped me understand how powerful NLP and LLMs are for solving real problems like answering university questions. Fine-tuning the T5 model on my own data made it give accurate and helpful answers for students. I faced challenges like handling different text lengths and cleaning duplicate data, but I learned how to fix them. Overall, I’m proud that my chatbot can save students time and make university information easier to access.

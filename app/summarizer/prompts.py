SUMMARY_PROMPT = """
You are a professional AI and Data Science technical writer.

Your task is to summarize the article below.

Rules:
1. Write 120-150 words.
2. Use simple English.
3. Mention the main technology.
4. Explain why it is important.
5. Don't invent information.
6. Return ONLY the summary.

Article Title:
{title}

Article Content:
{content}
"""
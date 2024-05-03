# Policy Impact Assessment Chatbot

This project develops a chatbot aimed at assessing the impact of government policies on vulnerable populations. The chatbot facilitates the collection and analysis of data regarding government initiatives, focusing on how these policies are implemented and their effects on marginalized groups. This tool is designed to support policymakers in making informed decisions that ensure equitable outcomes and address disparities effectively.

## Project Background

Policymakers often struggle to understand the full impact of policies on vulnerable populations, which can lead to unintended consequences that exacerbate challenges faced by these groups. By providing a conversational system that can gather and analyze feedback on policy implementation, this chatbot serves as a critical tool in ensuring that policies are supportive and effective.

## Features

- **Data Integration**: Utilizes a comprehensive dataset about government schemes stored in JSON and CSV formats.
- **Social Media Insights**: Retrieves relevant discussions from platforms like Reddit and Twitter, providing real-time public sentiment analysis.
- **Advanced Analytics**: Employs a pre-trained and fine-tuned chatbot model to interpret responses and generate actionable insights.
- **Report Generation**: Automatically compiles findings into structured reports for easy consumption by policymakers.

## Dataset
- **Government Schemes Data**: We outline the data collection process of the policies from the web-site https://www.myscheme.gov.in/. The objective was to gather information about various government schemes listed on the web-site, organize it by state and ministry, and compile the data into a structured format for further analysis. Since there was no API or predefined dataset to gather this information, we utilized web-scrapping methods manually to find the relevant information regarding the policies. Additionally, our focus was on state policies that predominantly affect vulnerable populations.
- **X Data**: The dataset consists of structured information from tweets, each represented by attributes including ID, date, URL, full text, favourite count, and retweet count. This data was collected using an Apify actor configured to scrape Twitter based on specific parameters such as the maximum number of tweets and inclusion of user info. Post-collection, the data underwent preprocessing to remove irrelevant entries, and relevant tweet details were then extracted and stored in a structured format. Finally, this data was organized into a pandas DataFrame and saved as "rawtweets.csv" for further analysis.
- **Reddit Data**: The dataset comprises structured information from Reddit posts, with attributes including Id, Url, title, date, content, and community name. Data collection was facilitated by using the Apify client to invoke the trudax/reddit-scraper actor, configured via the raw input dictionary. After retrieving the posts, I processed and extracted pertinent information, which was then organized into the ‘reddit posts’ dictionary. This processed data was converted into a pandas DataFrame and subsequently saved as "raw-reddit-posts.csv" for further analysis.

## Instructions to run the Chatbot
<li> Install the django using command "pip install django"
<li>Change the directory to chatbotui and start the server using the command "python3 manage.py runserver"  

## Youtube link
<a href="https://youtu.be/5A3tYNWGA64">https://youtu.be/5A3tYNWGA64</a>

## Comparison with baselines and the system's performance on existing data and SOTA on different evaluation metrics and how the system performs on new data / handles different cases.
The intricately structured model prompt template significantly elevates the functionality of the LLM by meticulously assigning specific roles, thereby refining the quality and relevance of its responses. In our case, both LangChain and Llama are provided with a prompt template that meticulously details the content and structure of the input data: a CSV file containing social media posts with analyzed sentiments and pertinent information regarding various government schemes. This directive ensures that the models initially refer to the document for relevant data, leveraging the pre-analyzed information to enhance the accuracy and relevance of their responses.

If the necessary information is not found within the document, the models are then instructed to autonomously generate responses based on their built-in capabilities. This tiered approach not only ensures completeness and precision in the output but also plays a critical role in maintaining the integrity of the data by mitigating the risk of incorporating spurious or inaccurate information.

Moreover, if the models encounter inputs that are ambiguous or beyond their current understanding, they are programmed to gracefully output an apology and request the user to resubmit the query with a clearer prompt. This safeguard is crucial for maintaining user engagement and trust, especially in scenarios where clear communication is paramount for effective information retrieval and decision-making.

By employing such a rigorous and structured approach, the performance of these models can be directly compared against existing baselines and state-of-the-art (SOTA) systems using a variety of evaluation metrics. This methodical evaluation helps in not only highlighting the areas where our system excels but also in identifying opportunities for further enhancements.

Furthermore, the robustness of this approach is tested against new and varying datasets to assess how well the system adapts to different cases and data nuances. This dynamic assessment helps in understanding the flexibility and scalability of the system in real-world applications, ensuring that it remains effective and efficient across a broad spectrum of scenarios and continues to deliver high-quality outputs that align with user expectations and industry standards.



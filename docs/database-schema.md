Initial Tables: 


 ├── User  
        ├── id
        ├── name
        ├── email
        ├── craeted_at

 ├── Profiles
        ├──id
        ├── user_id
        ├── age
        ├── profession
        ├── language
        ├── voice_preference

 ├── interests
        ├──id
        ├──name

 ├── user_interests
        ├── user_id
        ├── interest_id

 ├── news_articles
        ├── id
        ├── title
        ├── category
        ├── published_at
        ├── source
        ├── full_content

 ├── summaries
        ├── id
        ├── article_id
        ├── quick_summary
        ├── detailed_summary

 ├── audio_briefings
        ├── id
        ├── article_id
        ├── audio_url
        ├── voice_type
 
 ├── news_sessions
        ├── id
        ├── user_id
        ├── session_time
        ├── selected_duration
        ├── created_at
        ├── selected_mode
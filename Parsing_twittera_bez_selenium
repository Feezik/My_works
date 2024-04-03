import requests
import json
import codecs
from datetime import datetime


# Параметры прокси (нужно проверить работает ли прокси сервер)
proxy_host = "189.240.60.168"
proxy_port = 9090

# URL для получения твитов пользователя
url = 'https://api.twitter.com/graphql/GA3HM3gm-TtZJNVsvnF5Yg/UserTweets'


# Настройка прокси
proxies = {
    "http": f"http://{proxy_host}:{proxy_port}",
}

# Параметры запроса для удаления не нужных данных
query_params = {
    'variables': '{"userId":"44196397","count":10,"includePromotedContent":false,"withQuickPromoteEligibilityTweetFields":false ,"withVoice":true,"withV2Timeline":true}',
    'features': '{"responsive_web_graphql_exclude_directive_enabled":false,"verified_phone_label_enabled":false,"creator_subscriptions_tweet_preview_api_enabled":false,"responsive_web_graphql_timeline_navigation_enabled":false,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"communities_web_enable_tweet_community_results_fetch":false,"c9s_tweet_anatomy_moderator_badge_enabled":false,"tweetypie_unmention_optimization_enabled":false,"responsive_web_edit_tweet_api_enabled":false,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":false,"view_counts_everywhere_api_enabled":false,"longform_notetweets_consumption_enabled":false,"responsive_web_twitter_article_tweet_consumption_enabled":false,"tweet_awards_web_tipping_enabled":false,"freedom_of_speech_not_reach_fetch_enabled":false,"standardized_nudges_misinfo":false,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":false,"rweb_video_timestamps_enabled":false,"longform_notetweets_rich_text_read_enabled":false,"longform_notetweets_inline_media_enabled":false,"responsive_web_enhance_cards_enabled":false}',
    'fieldToggles': '{"withArticlePlainText":false}'
}

# Заголовки запроса
headers = {
    'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'X-Guest-Token': '1775100760650387743' # Нужно проверить токен 
}

# Отправить GET-запрос с токеном авторизации
response = requests.get(url, proxies=proxies, params=query_params, headers=headers)

if response.status_code == 200:
    # Разобрать JSON-ответ
    data = response.json()
    
    posts = []

    ROUTE_TO_INSTRUCTIONS = ['data', 'user', 'result', 'timeline_v2', 'timeline', 'instructions']

    ROUTE_TO_TWIT_LEGACY = ['content', 'itemContent', 'tweet_results', 'result', 'legacy']

    instructions = data
    for route in ROUTE_TO_INSTRUCTIONS:
        instructions = instructions[route]

    entries = []
    for instruction in instructions:
        if instruction['type'] == 'TimelineAddEntries':
            entries = instruction['entries']
            break

    for entery in entries:
        legacy = entery
        for route in ROUTE_TO_TWIT_LEGACY:
            legacy = legacy[route]

        date = legacy['created_at']
        text = legacy['full_text']

        posts.append((datetime.strptime(date, "%a %b %d %H:%M:%S +0000 %Y"), text))

    print("  ****  POSTS  ****  ")
    posts.sort(reverse=True)
    for post in posts[:10]:
        print(post[1])
        print(post[0].strftime("%Y-%m-%d %H:%M:%S"))
        print()

else:
    print(f'Ошибка: {response.status_code}')

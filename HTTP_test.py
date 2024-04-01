import requests
import json
from datetime import datetime

# URL для получения твитов пользователя
url = 'https://api.twitter.com/graphql/GA3HM3gm-TtZJNVsvnF5Yg/UserTweets'

# Параметры запроса
query_params = {
    'variables': '{"userId":"44196397","count":10,"includePromotedContent":false,"withQuickPromoteEligibilityTweetFields":false ,"withVoice":true,"withV2Timeline":true}',
    'features': '{"responsive_web_graphql_exclude_directive_enabled":false,"verified_phone_label_enabled":false,"creator_subscriptions_tweet_preview_api_enabled":false,"responsive_web_graphql_timeline_navigation_enabled":false,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"communities_web_enable_tweet_community_results_fetch":false,"c9s_tweet_anatomy_moderator_badge_enabled":false,"tweetypie_unmention_optimization_enabled":false,"responsive_web_edit_tweet_api_enabled":false,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":false,"view_counts_everywhere_api_enabled":false,"longform_notetweets_consumption_enabled":false,"responsive_web_twitter_article_tweet_consumption_enabled":false,"tweet_awards_web_tipping_enabled":false,"freedom_of_speech_not_reach_fetch_enabled":false,"standardized_nudges_misinfo":false,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":false,"rweb_video_timestamps_enabled":false,"longform_notetweets_rich_text_read_enabled":false,"longform_notetweets_inline_media_enabled":false,"responsive_web_enhance_cards_enabled":false}',
    'fieldToggles': '{"withArticlePlainText":false}'
}

# Заголовки запроса
headers = {
    'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'X-Guest-Token': '1774743496819081431' # Нужно проверить токен 
}

# Отправить GET-запрос с токеном авторизации
response = requests.get(url, params=query_params, headers=headers)

if response.status_code == 200:
    # Разобрать JSON-ответ
    data = response.json()
    # Сохранить JSON-ответ в файл
    with open('twitter_response_1.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print('Ответ сохранен в файл twitter_response_1.json')


else:
    print(f'Ошибка: {response.status_code}')



# Загрузка JSON-данных
with open('twitter_response_1.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Извлечение инструкций
instructions = data['data']['user']['result']['timeline_v2']['timeline']['instructions']

# Обработка твитов
tweets = []
for instruction in instructions:
    if instruction['type'] == 'TimelinePinEntry':
        entry = instruction['entry']
        content = entry['content']
        item_content = content['itemContent']

        # Проверка типа элемента
        if item_content['itemType'] == "TimelineTweet":
            tweet_results = item_content['tweet_results']
            result = tweet_results['result']
            legacy = result['legacy']
            full_text = legacy['full_text']
            created_at = legacy['created_at']

            # Обработка даты и времени
            created_at_dt = datetime.strptime(created_at, '%a %b %d %H:%M:%S %z %Y')
            print(f"Добавлен твит: {full_text}")

            tweets.append((created_at_dt, full_text))

# Сортировка твитов
tweets.sort(key=lambda x: x[0], reverse=True)

for i, tweet in enumerate(tweets[:10]):
    print('--------------')
    print(f"Твит {i + 1}: {tweet[1]}")
    print(f"Дата публикации: {tweet[0]}")

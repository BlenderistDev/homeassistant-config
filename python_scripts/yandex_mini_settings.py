isActivationSound = hass.states.is_state('input_boolean.alica_activation_sound', 'on')
isDj = hass.states.is_state('input_boolean.alica_dj', 'on')
isNoWords = hass.states.is_state('input_boolean.alica_no_words', 'on')
isWhisper = hass.states.is_state('input_boolean.alica_whisper', 'on')

states = [isActivationSound, isDj, isNoWords, isWhisper]
commands = ['звук активации: ', 'анонсировать треки: ', 'без лишних слов: ', 'ответить шепотом: ']

YES_SUFFIX = 'да'
NOT_SUFFIX = 'нет'

for i in range(len(states)):
    if states[i]:
        command = commands[i] + YES_SUFFIX
    else:
        command = commands[i] + NOT_SUFFIX

    # https://github.com/AlexxIT/YandexStation#%D0%B8%D0%B7%D0%BC%D0%B5%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B5%D0%BA-%D0%B0%D0%BB%D0%B8%D1%81%D1%8B
    data = {
        'media_content_id': command,
        'media_content_type': 'settings',
        'entity_id': 'media_player.yandex_station_ff98f029e3e3e2ddfdbd1676',
    }
    
    hass.services.call(
        "media_player",
        "play_media",
        data
    )
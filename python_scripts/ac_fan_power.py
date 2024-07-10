reverse = data.get('reverse')
entity_id = data.get('entity_id')

powerInput = hass.states.get(entity_id).attributes['fan_mode']

powerOutput = ''

if (reverse):
    if powerInput == 'mute':
        powerOutput = 'mute'
    if powerInput == 'low':
        powerOutput = 'mute'
    if powerInput == 'medium':
        powerOutput = 'low'
    if powerInput == 'high':
        powerOutput = 'medium'
    if powerInput == 'turbo':
        powerOutput = 'high'
else:
    if powerInput == 'mute':
        powerOutput = 'low'
    if powerInput == 'low':
        powerOutput = 'medium'
    if powerInput == 'medium':
        powerOutput = 'high'
    if powerInput == 'high':
        powerOutput = 'turbo'
    if powerInput == 'turbo':
        powerOutput = 'turbo'

data = {
    'entity_id': entity_id,
    'fan_mode': powerOutput,
}

hass.services.call(
    "climate",
    "set_fan_mode",
    data
)
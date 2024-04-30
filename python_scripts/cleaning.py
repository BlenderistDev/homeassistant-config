type = data.get('type')

vacuumMode = 'Sweep'
if type == 'sweep':
    vacuumMode = 'Sweep'
if type == 'mop':
    vacuumMode = 'Mop'
if type == 'sweepmop':
    vacuumMode = 'Sweep And Mop'

hass.services.call(
    'select',
    'select_option',
    {
        'option': vacuumMode,
        'entity_id': 'select.ijai_v18_af59_mode'
    },
    True
)

isBedroom = hass.states.is_state('input_boolean.clean_bedroom', 'on')
isLivingroom = hass.states.is_state('input_boolean.clean_livingroom', 'on')
isChildrenRoom = hass.states.is_state('input_boolean.clean_children_room', 'on')
isKitchen = hass.states.is_state('input_boolean.clean_kitchen', 'on')
isHallway = hass.states.is_state('input_boolean.clean_hallway', 'on')

roomsToClean = []
if isBedroom:
    roomsToClean.append('13')
if isLivingroom:
    roomsToClean.append('12')
if isChildrenRoom:
    roomsToClean.append('14')
if isKitchen:
    roomsToClean.append('10')
if isHallway:
    roomsToClean.append('17')
    
roomListStr = ",".join(roomsToClean)

# https://home.miot-spec.com/spec/ijai.vacuum.v18
data = {
    'siid': 7,
    'aiid': 3,
    'entity_id': 'vacuum.ijai_v18_af59_robot_cleaner',
    'params': [roomListStr, 0, 1],
}

hass.services.call(
    "xiaomi_miot",
    "call_action",
    data
)

hass.services.call("input_boolean", "turn_off", {'entity_id': 'input_boolean.clean_bedroom'})
hass.services.call("input_boolean", "turn_off", {'entity_id': 'input_boolean.clean_livingroom'})
hass.services.call("input_boolean", "turn_off", {'entity_id': 'input_boolean.clean_children_room'})
hass.services.call("input_boolean", "turn_off", {'entity_id': 'input_boolean.clean_kitchen'})
hass.services.call("input_boolean", "turn_off", {'entity_id': 'input_boolean.clean_hallway'})
reverse = data.get('reverse')

if (reverse):
    powerInput = hass.states.get('vacuum.ijai_v18_af59_robot_cleaner').attributes['fan_speed']

    powerOutput = ''
    if powerInput == 'Slient':
        powerOutput = 'Тихий'
    if powerInput == 'Standard':
        powerOutput = 'Стандартный'
    if powerInput == 'Medium':
        powerOutput = 'Средний'
    if powerInput == 'Turbo':
        powerOutput = 'Турбо'
    
    data = {
        'entity_id': 'input_select.vacuum_power',
        'option': powerOutput,
    }
    
    hass.services.call(
        "input_select",
        "select_option",
        data
    )
else:
    powerInput = hass.states.get('input_select.vacuum_power').state

    powerOutput = 'Turbo'
    if powerInput == 'Тихий':
        powerOutput = 'Slient'
    if powerInput == 'Стандартный':
        powerOutput = 'Standard'
    if powerInput == 'Средний':
        powerOutput = 'Medium'
    if powerInput == 'Турбо':
        powerOutput = 'Turbo'
    
    data = {
        'entity_id': 'vacuum.ijai_v18_af59_robot_cleaner',
        'fan_speed': powerOutput,
    }
    
    hass.services.call(
        "vacuum",
        "set_fan_speed",
        data
    )


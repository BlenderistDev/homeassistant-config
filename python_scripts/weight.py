weight = float(hass.states.get('sensor.ble_stabilized_weight_5ccad3406f9c').state)
impedance = float(hass.states.get('sensor.ble_impedance_5ccad3406f9c').state)

zhenyaMax = 50
helenMax = 85

if impedance != 0:
    if weight < zhenyaMax:
        hass.services.call("input_number", "set_value", {'entity_id': 'input_number.zhenya_wieght', 'value': weight})
        hass.services.call("input_number", "set_value", {'entity_id': 'input_number.zhenya_impedance', 'value': impedance})
    elif weight < helenMax:
        hass.services.call("input_number", "set_value", {'entity_id': 'input_number.helen_wieght', 'value': weight})
        hass.services.call("input_number", "set_value", {'entity_id': 'input_number.helen_impedance', 'value': impedance})
    else:
        hass.services.call("input_number", "set_value", {'entity_id': 'input_number.dmitry_wieght', 'value': weight})
        hass.services.call("input_number", "set_value", {'entity_id': 'input_number.dmitry_impedance', 'value': impedance})


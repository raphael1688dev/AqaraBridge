from homeassistant.components.binary_sensor import BinarySensorDeviceClass
from homeassistant.components.climate import (
    FAN_AUTO,
    FAN_HIGH,
    FAN_LOW,
    FAN_MEDIUM,
    PRESET_BOOST,
    PRESET_NONE,
    SWING_OFF,
    SWING_ON,
    ClimateEntityFeature,
    HVACMode,
)
from homeassistant.components.cover import (
    CoverDeviceClass,
    CoverEntityFeature,
    CoverState,
)
from homeassistant.components.event import EventDeviceClass
from homeassistant.components.light import ColorMode, LightEntityFeature
from homeassistant.components.sensor import SensorDeviceClass, SensorStateClass
from homeassistant.const import (
    CONCENTRATION_PARTS_PER_BILLION,
    LIGHT_LUX,
    PERCENTAGE,
    UnitOfEnergy,
    UnitOfPower,
    UnitOfTemperature,
)

from .const import (
    GESTURE_MAPPING,
    PET_MAPPING,
    HUMAN_MAPPING,
    MOVING_MAPPING,
    SOUND_MAPPING,
    KN_BUTTON_MAPPING,
    KN_BUTTON_3_MAPPING,
    KN_SLIDE_MAPPING,
    FP_MOTION_MAPPING,
)

# AiotDevice Mapping
MK_MAPPING_PARAMS = "mapping_params"
MK_INIT_PARAMS = "init_params"
MK_RESOURCES = "resources"
MK_HASS_NAME = "hass_attr_name"

AIOT_DEVICE_MAPPING = [
    ############################ Aqara M1SGateway###################################
    {
        "lumi.gateway.aeu01": ["Aqara", "Gateway M1S", "ZHWG15LM"],
        "lumi.gateway.acn01": ["Aqara", "Gateway M1S", "ZHWG15LM"],
        "lumi.gateway.acn004": ["Aqara", "Gateway M1S 22", "ZHWG15LM"],
        "lumi.gateway.acn008": ["Aqara", "Gateway M1S Gen2", ""],
        "lumi.gateway.agl002": ["Aqara", "Gateway M1S Gen2", "ZHWG15LM"],
        "lumi.gateway.aqhm02": ["Aqara", "Gateway", "ZHWG15LM"],
        "lumi.gateway.aqhm01": ["Aqara", "Gateway", "ZHWG15LM"],
        "params": [
            {
                "light": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "light",
                        "supported_features": LightEntityFeature.EFFECT,
                        "supported_color_modes": {ColorMode.RGB},
                        "color_mode": ColorMode.RGB,
                    },
                    MK_RESOURCES: {
                        "toggle": ("14.7.111", "_attr_is_on"),
                        "color": ("14.7.85", "_attr_rgb_color"),
                        "brightness": ("14.7.1006", "_attr_brightness"),
                    },
                }
            },
            {
                "sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "illuminance",
                        "device_class": SensorDeviceClass.ILLUMINANCE,
                        "state_class": SensorStateClass.MEASUREMENT,
                        "unit_of_measurement": LIGHT_LUX,
                    },
                    MK_RESOURCES: {"illumination": ("0.3.85", "_attr_native_value")},
                }
            },
        ],
    },
    ###########################Aqara H1, E1, M2, M3, Magicpad S1 Gateways#############################
    {
        "lumi.gateway.sacn01": ["Aqara", "Smart Hub H1", "QBCZWG11LM"],
        "lumi.gateway.aqcn02": ["Aqara", "Hub E1", "ZHWG16LM"],
        "lumi.gateway.iragl01": ["Aqara", "GateWay M2", ""],
        "lumi.gateway.iragl5": ["Aqara", "GateWay M2", ""],
        "lumi.gateway.iragl7": ["Aqara", "GateWay M2", ""],
        "lumi.gateway.iragl8": ["Aqara", "GateWay M2 22", ""],
        "lumi.gateway.aq1": ["Aqara", "GateWay M2", ""],
        "lumi.gateway.acn012": ["Aqara", "GateWay M3", ""],
        "lumi.controller.a4acn1": ["Aqara", "GateWay JY S1", ""],
        "params": [],
    },
    ###############################Gateway / Camera########################################
    {
        "lumi.camera.gwpagl01": ["Aqara", "Camera G3 (Gateway)", ""],
        "params": [
            {
                "event": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "camera",
                        "event_types": [
                            "1",
                            "2",
                            "3",
                            "4",
                            "5",
                            "6",
                            "7",
                            "8",
                            "9",
                            "10",
                        ],
                        "unique_id_extra": "face",
                        "entity_name": "Face Recognition",
                    },
                    MK_RESOURCES: {
                        "detect_face_event": ("13.95.85", "_attr_native_value"),
                    },
                }
            },
            {
                "event": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "camera",
                        "event_types_mapping": HUMAN_MAPPING,
                        "unique_id_extra": "human",
                        "entity_name": "Body Recognition",
                    },
                    MK_RESOURCES: {
                        "detect_human_event": ("13.97.85", "_attr_native_value"),
                    },
                }
            },
            {
                "event": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "camera",
                        "event_types_mapping": PET_MAPPING,
                        "unique_id_extra": "pet",
                        "entity_name": "Pet Recognition",
                    },
                    MK_RESOURCES: {
                        "detect_pets_event": ("13.98.85", "_attr_native_value"),
                    },
                }
            },
            {
                "event": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "camera",
                        "event_types_mapping": GESTURE_MAPPING,
                        "unique_id_extra": "gesture",
                        "entity_name": "Gesture Recognition",
                    },
                    MK_RESOURCES: {
                        "detect_gesture_event": ("13.96.85", "_attr_native_value"),
                    },
                }
            },
            {
                "event": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "camera",
                        "event_types_mapping": MOVING_MAPPING,
                        "unique_id_extra": "moving",
                        "entity_name": "Motion Detection",
                    },
                    MK_RESOURCES: {
                        "detect_moving_event": ("3.21.85", "_attr_native_value"),
                    },
                }
            },
            {
                "event": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "camera",
                        "event_types_mapping": SOUND_MAPPING,
                        "unique_id_extra": "sound",
                        "entity_name": "Abnormal Sound",
                    },
                    MK_RESOURCES: {
                        "detect_sound_event": ("3.22.85", "_attr_native_value"),
                    },
                }
            },
        ],
    },
    ################################Wall Switch#########################################
    ###Single Key
    {
        # Canon Smart Wall Switch Z1 Pro (Single Key)
        "lumi.switch.acn056": ["Aqara", "KN Wall Switch Z1 Pro (Single Rocker)", ""],
        "params": [
            {
                "switch": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "wall_switch",
                    },
                    MK_RESOURCES: {
                        "toggle": ("4.1.85", "_attr_is_on"),
                    },
                }
            },
            {
                "event": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "default",
                        "event_mapping": KN_BUTTON_MAPPING,
                        "entity_name": "Wireless Switch",
                    },
                    MK_RESOURCES: {"event": ("13.21.85", "_attr_trigger")},
                }
            },
            {
                "event": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "slide",
                        "event_mapping": KN_SLIDE_MAPPING,
                        "entity_name": "Slider",
                    },
                    MK_RESOURCES: {"event": ("13.1.85", "_attr_trigger")},
                }
            },
            {
                "sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "power",
                        "device_class": SensorDeviceClass.POWER,
                        "state_class": SensorStateClass.MEASUREMENT,
                        "unit_of_measurement": UnitOfPower.WATT,
                    },
                    MK_RESOURCES: {"current": ("0.14.85", "_attr_native_value")},
                }
            },
            {
                "sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "energy",
                        "device_class": SensorDeviceClass.ENERGY,
                        "state_class": "total_increasing",
                        "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
                    },
                    MK_RESOURCES: {"energy": ("0.13.85", "_attr_native_value")},
                }
            },
        ],
    },
    {
        # Canon Smart Wall Switch Z1 Pro (Double Keys)
        "lumi.switch.acn057": ["Aqara", "KN Wall Switch Z1 Pro (Double Rocker)", ""],
        "params": [
            {
                "switch": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "wall_switch",
                    },
                    MK_RESOURCES: {
                        "toggle": ("4.{}.85", "_attr_is_on"),
                    },
                    MK_MAPPING_PARAMS: {"ch_count": 2},
                }
            },
            {
                "event": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "default",
                        "event_mapping": KN_BUTTON_MAPPING,
                        "entity_name": "Wireless Switch",
                    },
                    MK_RESOURCES: {"event": ("13.{}.85", "_attr_trigger")},
                    MK_MAPPING_PARAMS: {"ch_count": 2, "ch_start": 21},
                }
            },
            {
                "event": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "slide",
                        "event_mapping": KN_SLIDE_MAPPING,
                        "entity_name": "Slider",
                    },
                    MK_RESOURCES: {"event": ("13.1.85", "_attr_trigger")},
                }
            },
            {
                "sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "power",
                        "device_class": SensorDeviceClass.POWER,
                        "state_class": SensorStateClass.MEASUREMENT,
                        "unit_of_measurement": UnitOfPower.WATT,
                    },
                    MK_RESOURCES: {"power": ("0.12.85", "_attr_native_value")},
                }
            },
            {
                "sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "energy",
                        "device_class": SensorDeviceClass.ENERGY,
                        "state_class": "total_increasing",
                        "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
                    },
                    MK_RESOURCES: {"energy": ("0.13.85", "_attr_native_value")},
                }
            },
        ],
    },
    {
        # Canon Smart Wall Switch Z1 Pro (Triple Keys)
        "lumi.switch.acn058": ["Aqara", "KN Wall Switch Z1 Pro (Three Rocker)", ""],
        "params": [
            {
                "switch": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "wall_switch",
                    },
                    MK_RESOURCES: {
                        "toggle": ("4.{}.85", "_attr_is_on"),
                    },
                    MK_MAPPING_PARAMS: {"ch_count": 3},
                }
            },
            {
                "event": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "default",
                        "event_mapping": KN_BUTTON_3_MAPPING,
                        "entity_name": "Wireless Switch",
                    },
                    MK_RESOURCES: {"event": ("13.{}.85", "_attr_trigger")},
                    MK_MAPPING_PARAMS: {"ch_count": 3, "ch_start": 21},
                }
            },
            {
                "event": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "slide",
                        "event_mapping": KN_SLIDE_MAPPING,
                        "entity_name": "Slider",
                    },
                    MK_RESOURCES: {"event": ("13.1.85", "_attr_trigger")},
                }
            },
            {
                "sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "power",
                        "device_class": SensorDeviceClass.POWER,
                        "state_class": SensorStateClass.MEASUREMENT,
                        "unit_of_measurement": UnitOfPower.WATT,
                    },
                    MK_RESOURCES: {"power": ("0.12.85", "_attr_native_value")},
                }
            },
            {
                "sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "energy",
                        "device_class": SensorDeviceClass.ENERGY,
                        "state_class": "total_increasing",
                        "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
                    },
                    MK_RESOURCES: {"energy": ("0.13.85", "_attr_native_value")},
                }
            },
        ],
    },
    {
        # Canon Smart Wall Switch Z1 Pro (Quadruple Keys)
        "lumi.switch.acn059": ["Aqara", "KN Wall Switch Z1 Pro (Four Rocker)", ""],
        # Smart Wall Switch Q1 (Quadruple Keys)
        "lumi.switch.acn065": ["Aqara", "Wall Switch Q1 (Four Rocker)", ""],
        "params": [
            {
                "switch": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "wall_switch",
                    },
                    MK_RESOURCES: {
                        "toggle": ("4.{}.85", "_attr_is_on"),
                    },
                    MK_MAPPING_PARAMS: {"ch_count": 3},
                }
            },
            {
                "event": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "default",
                        "event_mapping": KN_BUTTON_3_MAPPING,
                        "entity_name": "Wireless Switch",
                    },
                    MK_RESOURCES: {"event": ("13.{}.85", "_attr_trigger")},
                    MK_MAPPING_PARAMS: {"ch_count": 4, "ch_start": 21},
                }
            },
            {
                "event": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "slide",
                        "event_mapping": KN_SLIDE_MAPPING,
                        "entity_name": "Slider",
                    },
                    MK_RESOURCES: {"event": ("13.1.85", "_attr_trigger")},
                }
            },
            {
                "sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "power",
                        "device_class": SensorDeviceClass.POWER,
                        "state_class": SensorStateClass.MEASUREMENT,
                        "unit_of_measurement": UnitOfPower.WATT,
                    },
                    MK_RESOURCES: {"power": ("0.12.85", "_attr_native_value")},
                }
            },
            {
                "sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "energy",
                        "device_class": SensorDeviceClass.ENERGY,
                        "state_class": "total_increasing",
                        "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
                    },
                    MK_RESOURCES: {"energy": ("0.13.85", "_attr_native_value")},
                }
            },
        ],
    },
    {
        # Canon Smart Wall Switch Z1 (Single Key)
        "lumi.switch.acn054": ["Aqara", "KN Wall Switch Z1 (Single Rocker)", ""],
        "params": [
            {
                "switch": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "wall_switch",
                    },
                    MK_RESOURCES: {
                        "toggle": ("4.1.85", "_attr_is_on"),
                    },
                }
            },
            {
                "event": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "default",
                        "event_mapping": KN_BUTTON_MAPPING,
                        "entity_name": "Wireless Switch",
                    },
                    MK_RESOURCES: {"event": ("13.21.85", "_attr_trigger")},
                }
            },
            {
                "sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "power",
                        "device_class": SensorDeviceClass.POWER,
                        "state_class": SensorStateClass.MEASUREMENT,
                        "unit_of_measurement": UnitOfPower.WATT,
                    },
                    MK_RESOURCES: {"power": ("0.12.85", "_attr_native_value")},
                }
            },
            {
                "sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "energy",
                        "device_class": SensorDeviceClass.ENERGY,
                        "state_class": "total_increasing",
                        "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
                    },
                    MK_RESOURCES: {"energy": ("0.13.85", "_attr_native_value")},
                }
            },
        ],
    },
    {
        # Canon Smart Wall Switch Z1 (Double Keys)
        "lumi.switch.acn054": ["Aqara", "KN Wall Switch Z1 (Double Rocker)", ""],
        "params": [
            {
                "switch": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "wall_switch",
                    },
                    MK_RESOURCES: {
                        "toggle": ("4.{}.85", "_attr_is_on"),
                    },
                    MK_MAPPING_PARAMS: {"ch_count": 2},
                }
            },
            {
                "event": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "default",
                        "event_mapping": KN_BUTTON_3_MAPPING,
                        "entity_name": "Wireless Switch",
                    },
                    MK_RESOURCES: {"event": ("13.{}.85", "_attr_trigger")},
                    MK_MAPPING_PARAMS: {"ch_count": 2, "ch_start": 21},
                }
            },
            {
                "sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "power",
                        "device_class": SensorDeviceClass.POWER,
                        "state_class": SensorStateClass.MEASUREMENT,
                        "unit_of_measurement": UnitOfPower.WATT,
                    },
                    MK_RESOURCES: {"power": ("0.12.85", "_attr_native_value")},
                }
            },
            {
                "sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "energy",
                        "device_class": SensorDeviceClass.ENERGY,
                        "state_class": "total_increasing",
                        "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
                    },
                    MK_RESOURCES: {"energy": ("0.13.85", "_attr_native_value")},
                }
            },
        ],
    },
    {
        # Canon Smart Wall Switch Z1 (Triple Keys)
        "lumi.switch.acn054": ["Aqara", "KN Wall Switch Z1 (Three Rocker)", ""],
        "params": [
            {
                "switch": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "wall_switch",
                    },
                    MK_RESOURCES: {
                        "toggle": ("4.{}.85", "_attr_is_on"),
                    },
                    MK_MAPPING_PARAMS: {"ch_count": 3},
                }
            },
            {
                "event": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "default",
                        "event_mapping": KN_BUTTON_3_MAPPING,
                        "entity_name": "Wireless Switch",
                    },
                    MK_RESOURCES: {"event": ("13.{}.85", "_attr_trigger")},
                    MK_MAPPING_PARAMS: {"ch_count": 3, "ch_start": 21},
                }
            },
            {
                "sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "power",
                        "device_class": SensorDeviceClass.POWER,
                        "state_class": SensorStateClass.MEASUREMENT,
                        "unit_of_measurement": UnitOfPower.WATT,
                    },
                    MK_RESOURCES: {"power": ("0.12.85", "_attr_native_value")},
                }
            },
            {
                "sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "energy",
                        "device_class": SensorDeviceClass.ENERGY,
                        "state_class": "total_increasing",
                        "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
                    },
                    MK_RESOURCES: {"energy": ("0.13.85", "_attr_native_value")},
                }
            },
        ],
    },
    {
        # Canon Smart Wall Switch Z1 (Quadruple Keys)
        "lumi.switch.acn055": ["Aqara", "KN Wall Switch Z1 (Four Rocker)", ""],
        "params": [
            {
                "switch": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "wall_switch",
                    },
                    MK_RESOURCES: {
                        "toggle": ("4.{}.85", "_attr_is_on"),
                    },
                    MK_MAPPING_PARAMS: {"ch_count": 3},
                }
            },
            {
                "event": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "default",
                        "event_mapping": KN_BUTTON_3_MAPPING,
                        "entity_name": "Wireless Switch",
                    },
                    MK_RESOURCES: {"event": ("13.{}.85", "_attr_trigger")},
                    MK_MAPPING_PARAMS: {"ch_count": 4, "ch_start": 21},
                }
            },
            {
                "sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "power",
                        "device_class": SensorDeviceClass.POWER,
                        "state_class": SensorStateClass.MEASUREMENT,
                        "unit_of_measurement": UnitOfPower.WATT,
                    },
                    MK_RESOURCES: {"power": ("0.12.85", "_attr_native_value")},
                }
            },
            {
                "sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "energy",
                        "device_class": SensorDeviceClass.ENERGY,
                        "state_class": "total_increasing",
                        "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
                    },
                    MK_RESOURCES: {"energy": ("0.13.85", "_attr_native_value")},
                }
            },
        ],
    },
    {
        # Smart Wall Switch Q1 (Single Key)
        "lumi.switch.acn062": ["Aqara", "Wall Switch Q1 (Single Rocker)", ""],
        "params": [
            {
                "switch": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "wall_switch",
                    },
                    MK_RESOURCES: {
                        "toggle": ("4.1.85", "_attr_is_on"),
                    },
                }
            },
            {
                "event": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "default",
                        "event_mapping": KN_BUTTON_MAPPING,
                        "entity_name": "Wireless Switch",
                    },
                    MK_RESOURCES: {"event": ("13.21.85", "_attr_trigger")},
                }
            },
            {
                "event": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "slide",
                        "event_mapping": KN_SLIDE_MAPPING,
                        "entity_name": "Slider",
                    },
                    MK_RESOURCES: {"event": ("13.1.85", "_attr_trigger")},
                }
            },
            {
                "sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "power",
                        "device_class": SensorDeviceClass.POWER,
                        "state_class": SensorStateClass.MEASUREMENT,
                        "unit_of_measurement": UnitOfPower.WATT,
                    },
                    MK_RESOURCES: {"power": ("0.12.85", "_attr_native_value")},
                }
            },
            {
                "sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "energy",
                        "device_class": SensorDeviceClass.ENERGY,
                        "state_class": "total_increasing",
                        "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
                    },
                    MK_RESOURCES: {"energy": ("0.13.85", "_attr_native_value")},
                }
            },
        ],
    },
    {
        # Smart Wall Switch Q1 (Double Keys)
        "lumi.switch.acn063": ["Aqara", "KN Wall Switch Q1 (Double Rocker)", ""],
        "params": [
            {
                "switch": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "wall_switch",
                    },
                    MK_RESOURCES: {
                        "toggle": ("4.{}.85", "_attr_is_on"),
                    },
                    MK_MAPPING_PARAMS: {"ch_count": 2},
                }
            },
            {
                "event": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "slide",
                        "event_mapping": KN_SLIDE_MAPPING,
                        "entity_name": "Slider",
                    },
                    MK_RESOURCES: {"event": ("13.1.85", "_attr_trigger")},
                }
            },
            {
                "sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "power",
                        "device_class": SensorDeviceClass.POWER,
                        "state_class": SensorStateClass.MEASUREMENT,
                        "unit_of_measurement": UnitOfPower.WATT,
                    },
                    MK_RESOURCES: {"power": ("0.12.85", "_attr_native_value")},
                }
            },
            {
                "sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "energy",
                        "device_class": SensorDeviceClass.ENERGY,
                        "state_class": "total_increasing",
                        "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
                    },
                    MK_RESOURCES: {"energy": ("0.13.85", "_attr_native_value")},
                }
            },
        ],
    },
    {
        # Wall Switch (Neutral, Single Key)
        "lumi.ctrl_ln1.v1": ["Aqara", "Wall Switch (Single Rocker)", ""],
        # Wall Switch H1M (Neutral, Single Key)
        "lumi.switch.acn029": ["Aqara", "Wall Switch H1M (Single Rocker)", ""],
        # Wall Switch X1 (Neutral, Single Key)
        "lumi.switch.acn004": ["Aqara", "Wall Switch X1 (Single Rocker)", ""],
        # Wall Switch H1 (Neutral, Single Key)
        "lumi.switch.n1acn1": ["Aqara", "Wall Switch H1 (Single Rocker)", "QBKG27LM"],
        # Wall Switch T1 (Neutral, Single Key)
        "lumi.switch.b1nacn01": ["Aqara", "Wall Switch T1 (Single Rocker)", ""],
        # Wall Switch D1 (Neutral, Single Key)
        "lumi.switch.b1nacn02": ["Aqara", "Wall Switch D1 (Single Rocker)", ""],
        # Wall Switch E1 (Neutral, Single Key)
        "lumi.switch.b1nc01": ["Aqara", "Wall Switch E1 (Single Rocker)", ""],
        # Smart Wall Switch J1 (Neutral, Single Key)
        "lumi.switch.acn044": ["Aqara", "Wall Switch J1 (Single Rocker)", ""],
        "params": [
            {
                "switch": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "wall_switch",
                    },
                    MK_RESOURCES: {
                        "toggle": ("4.1.85", "_attr_is_on"),
                        "zigbee_lqi": ("8.0.2007", "_attr_zigbee_lqi"),
                    },
                }
            },
            {
                "sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "power",
                        "device_class": SensorDeviceClass.POWER,
                        "state_class": SensorStateClass.MEASUREMENT,
                        "unit_of_measurement": UnitOfPower.WATT,
                    },
                    MK_RESOURCES: {"power": ("0.12.85", "_attr_native_value")},
                }
            },
            {
                "sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "energy",
                        "device_class": SensorDeviceClass.ENERGY,
                        "state_class": "total_increasing",
                        "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
                    },
                    MK_RESOURCES: {"energy": ("0.13.85", "_attr_native_value")},
                }
            },
        ],
    },
    {
        # Wall Switch (No Neutral, Single Key)
        "lumi.ctrl_neutral1.v1": ["Aqara", "Wall Switch (Single Rocker)", "QBKG04LM"],
        # Wall Switch X1 (No Neutral, Single Key)
        "lumi.switch.acn001": ["Aqara", "Wall Switch X1 (Single Rocker)", ""],
        # Wall Switch H1 (No Neutral, Single Key)
        "lumi.switch.l1acn1": ["Aqara", "Wall Switch H1 (Single Rocker)", "QBKG27LM"],
        # Wall Switch T1 (No Neutral, Single Key)
        "lumi.switch.b1lacn01": ["Aqara", "Wall Switch T1 (Single Rocker)", ""],
        # Wall Switch D1 (No Neutral, Single Key)
        "lumi.switch.b1lacn02": ["Aqara", "Wall Switch D1 (Single Rocker)", ""],
        # Wall Switch E1 (No Neutral, Single Key)
        "lumi.switch.b1lc04": ["Aqara", "Wall Switch E1 (Single Rocker)", ""],
        # Wall SwitchJ1（No Neutral Single Key）
        "lumi.switch.acn041": ["Aqara", "Wall Switch J1 (Single Rocker)", ""],
        "params": [
            {
                "switch": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "wall_switch",
                    },
                    MK_RESOURCES: {
                        "toggle": ("4.1.85", "_attr_is_on"),
                        "zigbee_lqi": ("8.0.2007", "_attr_zigbee_lqi"),
                    },
                }
            }
        ],
    },
    ###Double Keys
    {
        # Wall Switch（Neutral Double Keys）
        "lumi.ctrl_ln2.v1": ["Aqara", "Wall Switch (Double Rocker)", ""],
        # Wall Switch H1M (Neutral, Double Keys)
        "lumi.switch.acn030": ["Aqara", "Wall Switch H1M (Double Rocker)", ""],
        # Wall Switch X1 (Neutral, Double Keys)
        "lumi.switch.acn005": ["Aqara", "Wall Switch X1 (Double Rocker)", ""],
        # Wall Switch H1 (Neutral, Double Keys)
        "lumi.switch.n2acn1": ["Aqara", "Wall Switch H1 (Double Rocker)", "QBKG27LM"],
        # Wall Switch T1 (Neutral, Double Keys)
        "lumi.switch.b2nacn01": ["Aqara", "Wall Switch T1 (Double Rocker)", ""],
        # Wall Switch D1 (Neutral, Double Keys)
        "lumi.switch.b2nacn02": ["Aqara", "Wall Switch D1 (Double Rocker)", ""],
        # Wall Switch E1 (Neutral, Double Keys)
        "lumi.switch.b2nc01": ["Aqara", "Wall Switch E1 (Double Rocker)", ""],
        "params": [
            {
                "switch": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "wall_switch",
                    },
                    MK_RESOURCES: {
                        "toggle": ("4.{}.85", "_attr_is_on"),
                        "zigbee_lqi": ("8.0.2007", "_attr_zigbee_lqi"),
                    },
                    MK_MAPPING_PARAMS: {"ch_count": 2},
                }
            },
            {
                "sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "power",
                        "device_class": SensorDeviceClass.POWER,
                        "state_class": SensorStateClass.MEASUREMENT,
                        "unit_of_measurement": UnitOfPower.WATT,
                    },
                    MK_RESOURCES: {"power": ("0.12.85", "_attr_native_value")},
                }
            },
            {
                "sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "energy",
                        "device_class": SensorDeviceClass.ENERGY,
                        "state_class": "total_increasing",
                        "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
                    },
                    MK_RESOURCES: {"energy": ("0.13.85", "_attr_native_value")},
                }
            },
        ],
    },
    {
        # Smart Wall Switch J1 (Neutral, Double Keys)
        "lumi.switch.acn045": ["Aqara", "Wall Switch J1 (Double Rocker)", ""],
        "params": [
            {
                "switch": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "wall_switch",
                    },
                    MK_RESOURCES: {
                        "toggle": ("4.{}.85", "_attr_is_on"),
                        "zigbee_lqi": ("8.0.2007", "_attr_zigbee_lqi"),
                    },
                    MK_MAPPING_PARAMS: {"ch_count": 2},
                }
            },
            {
                "sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "energy",
                        "device_class": SensorDeviceClass.ENERGY,
                        "state_class": "total_increasing",
                        "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
                    },
                    MK_RESOURCES: {"energy": ("0.13.85", "_attr_native_value")},
                }
            },
        ],
    },
    {
        # Wall Switch（No Neutral Double Keys）
        "lumi.ctrl_neutral2.v1": ["Aqara", "Wall Switch (Double Rocker)", "QBKG04LM"],
        # Wall Switch X1 (No Neutral, Double Keys)
        "lumi.switch.acn002": ["Aqara", "Wall Switch X1 (Double Rocker)", ""],
        # Wall Switch H1 (No Neutral, Double Keys)
        "lumi.switch.l2acn1": ["Aqara", "Wall Switch H1 (Double Rocker)", "QBKG28LM"],
        # Wall Switch T1 (No Neutral, Double Keys)
        "lumi.switch.b2lacn01": ["Aqara", "Wall Switch T1 (Double Rocker)", ""],
        # Wall Switch D1 (No Neutral, Double Keys)
        "lumi.switch.b2lacn02": ["Aqara", "Wall Switch D1 (Double Rocker)", "QBKG21LM"],
        # Wall Switch E1 (No Neutral, Double Keys)
        "lumi.switch.b2lc04": ["Aqara", "Wall Switch E1 (Double Rocker)", "QBKG21LM"],
        # Smart Wall Switch J1 (No Neutral, Double Keys)
        "lumi.switch.acn042": ["Aqara", "Wall Switch J1 (Double Rocker)", ""],
        "params": [
            {
                "switch": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "wall_switch",
                    },
                    MK_RESOURCES: {
                        "toggle": ("4.{}.85", "_attr_is_on"),
                        "zigbee_lqi": ("8.0.2007", "_attr_zigbee_lqi"),
                    },
                    MK_MAPPING_PARAMS: {"ch_count": 2},
                }
            }
        ],
    },
    ###Triple Keys
    {
        # Wall Switch H1M (Neutral, Triple Keys)
        "lumi.switch.acn031": ["Aqara", "Wall Switch H1M (Three Rocker)", ""],
        # Wall Switch X1 (Neutral, Triple Keys)
        "lumi.switch.acn006": ["Aqara", "Wall Switch X1 (Three Rocker)", ""],
        # Wall SwitchH1（Neutral Triple Keys）
        "lumi.switch.n3acn1": ["Aqara", "Wall Switch H1 (Three Rocker)", "QBKG27LM"],
        # Wall SwitchT1（Neutral Triple Keys）
        "lumi.switch.b3n01": ["Aqara", "Wall Switch T1 (Three Rocker)", ""],
        # SmartScene Panel Switch S1（Neutral Triple Keys）
        "lumi.switch.n4acn4": ["Aqara", "screen panel S1 (Three Rocker)", ""],
        # SmartWall Switch D1 (Neutral, Triple Keys)
        "lumi.switch.n3acn3": ["Aqara", "Wall Switch D1 (Three Rocker)", ""],
        "params": [
            {
                "switch": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "wall_switch",
                    },
                    MK_RESOURCES: {
                        "toggle": ("4.{}.85", "_attr_is_on"),
                        "zigbee_lqi": ("8.0.2007", "_attr_zigbee_lqi"),
                    },
                    MK_MAPPING_PARAMS: {"ch_count": 3},
                }
            },
            {
                "sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "power",
                        "device_class": SensorDeviceClass.POWER,
                        "state_class": SensorStateClass.MEASUREMENT,
                        "unit_of_measurement": UnitOfPower.WATT,
                    },
                    MK_RESOURCES: {"power": ("0.12.85", "_attr_native_value")},
                }
            },
            {
                "sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "energy",
                        "device_class": SensorDeviceClass.ENERGY,
                        "state_class": "total_increasing",
                        "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
                    },
                    MK_RESOURCES: {"energy": ("0.13.85", "_attr_native_value")},
                }
            },
        ],
    },
    {
        # SmartWall Switch E1（Neutral Triple Keys）
        "lumi.switch.acn040": ["Aqara", "Wall Switch E1 (Three Rocker)", ""],
        # Smart Wall Switch J1 (Neutral, Triple Keys)
        "lumi.switch.acn046": ["Aqara", "Wall Switch J1 (Three Rocker)", ""],
        # Magic Switch V1（Quadruple Keys version）
        "lumi.switch.acn051": ["Aqara", "Wall Switch V1", ""],
        # Starry Knob V1
        "lumi.switch.acn053": ["Aqara", "Wall Switch V1", ""],
        # Magic Switch S1E
        "lumi.switch.acn032": ["Aqara", "Wall Switch S1E", ""],
        "params": [
            {
                "switch": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "wall_switch",
                    },
                    MK_RESOURCES: {
                        "toggle": ("4.{}.85", "_attr_is_on"),
                    },
                    MK_MAPPING_PARAMS: {"ch_count": 3},
                }
            }
        ],
    },
    {
        # Wall Switch X1 (No Neutral, Triple Keys)
        "lumi.switch.acn003": ["Aqara", "Wall Switch X1 (Three Rocker)", ""],
        # Wall SwitchH1（No Neutral Triple Keys）
        "lumi.switch.l3acn1": ["Aqara", "Wall Switch H1 (Three Rocker)", "QBKG29LM"],
        # Wall SwitchT1（No Neutral Triple Keys）
        "lumi.switch.b3l01": ["Aqara", "Wall Switch T1 (Three Rocker)", ""],
        # SmartWall Switch D1 (No Neutral, Triple Keys)
        "lumi.switch.l3acn3": ["Aqara", "Wall Switch D1 (Three Rocker)", ""],
        "params": [
            {
                "switch": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "wall_switch",
                    },
                    MK_RESOURCES: {
                        "toggle": ("4.{}.85", "_attr_is_on"),
                        "zigbee_lqi": ("8.0.2007", "_attr_zigbee_lqi"),
                    },
                    MK_MAPPING_PARAMS: {"ch_count": 3},
                }
            }
        ],
    },
    {
        # Wall SwitchJ1（No Neutral Triple Keys）
        "lumi.switch.acn043": ["Aqara", "Wall Switch J1 (Three Rocker)", ""],
        "params": [
            {
                "switch": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "wall_switch",
                    },
                    MK_RESOURCES: {
                        "toggle": ("4.{}.85", "_attr_is_on"),
                    },
                    MK_MAPPING_PARAMS: {"ch_count": 3},
                }
            }
        ],
    },
    ##########################Switch Module、Socket Switch#######################################
    {
        # Single Channel Controller T1（No Neutral）
        "lumi.switch.l0acn1": ["Aqara", "Wall Switch (Single Rocker)", ""],
        # Single Channel Controller（Neutral）
        "lumi.switch.n0acn2": ["Aqara", "Wall Switch (Single Rocker)", ""],
        # Smart Plug (GB)
        "lumi.plug.v1": ["Xiaomi", "Plug", "ZNCZ02LM"],
        # Smart Plug (GB)
        "lumi.plug.aq1": ["Xiaomi", "Plug", ""],
        # Smart PlugT1 (GB)
        "lumi.plug.macn01": ["Aqara", "Plug T1", ""],
        # SmartWallSocket X1（USBversion）
        "lumi.plug.acn003": ["Aqara", "Smart Wall Outlet X1(USB)", ""],
        # SmartWallSocket H1（USBversion）
        "lumi.plug.sacn03": ["Aqara", "Smart Wall Outlet H1(USB)", "QBCZWG11LM"],
        # SmartWallSocket H1
        "lumi.plug.sacn02": ["Aqara", "Smart Wall Outlet H1", "QBCZWG11LM"],
        # WallSocket（Zigbeeversion）
        "lumi.ctrl_86plug.aq1": ["Aqara", "Plug AQ1", ""],
        "params": [
            {
                "switch": {
                    MK_INIT_PARAMS: {MK_HASS_NAME: "switch"},
                    MK_RESOURCES: {
                        "toggle": ("4.1.85", "_attr_is_on"),
                        "power": ("0.12.85", "_attr_current_power_w"),
                        "energy": ("0.13.85", "_attr_today_energy_kwh"),
                        "zigbee_lqi": ("8.0.2007", "_attr_zigbee_lqi"),
                    },
                }
            },
            {
                "sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "power",
                        "device_class": SensorDeviceClass.POWER,
                        "state_class": SensorStateClass.MEASUREMENT,
                        "unit_of_measurement": UnitOfPower.WATT,
                    },
                    MK_RESOURCES: {"power": ("0.12.85", "_attr_native_value")},
                }
            },
            {
                "sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "energy",
                        "device_class": SensorDeviceClass.ENERGY,
                        "state_class": "total_increasing",
                        "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
                    },
                    MK_RESOURCES: {"energy": ("0.13.85", "_attr_native_value")},
                }
            },
        ],
    },
    ###Dual Relay、Relay
    {
        # Dual Relay
        "lumi.relay.c2acn01": ["Aqara", "Double Way Controller", ""],
        # Dual Relay Module T2
        "lumi.switch.acn047": ["Aqara", "Double Way Controller T2", ""],
        "params": [
            {
                "switch": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "switch",
                    },
                    MK_RESOURCES: {
                        "toggle": ("4.{}.85", "_attr_is_on"),
                        "zigbee_lqi": ("8.0.2007", "_attr_zigbee_lqi"),
                    },
                    MK_MAPPING_PARAMS: {"ch_count": 2},
                }
            },
            {
                "sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "power",
                        "device_class": SensorDeviceClass.POWER,
                        "state_class": SensorStateClass.MEASUREMENT,
                        "unit_of_measurement": UnitOfPower.WATT,
                    },
                    MK_RESOURCES: {"power": ("0.12.85", "_attr_native_value")},
                }
            },
            {
                "sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "energy",
                        "device_class": SensorDeviceClass.ENERGY,
                        "state_class": "total_increasing",
                        "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
                    },
                    MK_RESOURCES: {"energy": ("0.13.85", "_attr_native_value")},
                }
            },
        ],
    },
    ###############################Dimmer###########################################
    # Brightness type
    {
        # Aqara Smart Constant Current Driver T1-1
        "lumi.light.cbacn1": ["Aqara", "Constant current driver T1", ""],
        # Track Grid Light H1 (6 heads)
        "lumi.light.acn007": ["Aqara", "H1 LED Light", ""],
        # Track Grid Light H1 (12 heads)
        "lumi.light.acn008": ["Aqara", "H1 LED Light", ""],
        # Track Flood Light H1 (30cm)
        "lumi.light.acn009": ["Aqara", "H1 LED Light", ""],
        # Track Flood Light H1 (60cm)
        "lumi.light.acn010": ["Aqara", "H1 LED Light", ""],
        # Track Pendant Light H1
        "lumi.light.acn011": ["Aqara", "H1 LED Light", ""],
        # Track Folding Grid Light H1 (6 heads)
        "lumi.light.acn012": ["Aqara", "H1 LED Light", ""],
        # Track Polarized Light H1 (22cm)
        "lumi.light.acn013": ["Aqara", "H1 LED Light", ""],
        "params": [
            {
                "light": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "light",
                        "supported_features": LightEntityFeature.EFFECT,
                        "supported_color_modes": {
                            ColorMode.BRIGHTNESS,
                        },
                        "color_mode": ColorMode.BRIGHTNESS,
                    },
                    MK_RESOURCES: {
                        "toggle": ("4.1.85", "_attr_is_on"),
                        "brightness": ("14.1.85", "_attr_brightness"),
                    },
                }
            }
        ],
    },
    # Color Temp type
    {
        # LEDBulb（Adjustable Color Temp）
        "lumi.light.aqcn02": ["Aqara", "Bulb", "ZNLDP12LM"],
        # Ceiling Light MX960 (Color Temp adjustable)
        "lumi.light.cwopcn01": ["Aqara", "Opple MX960", "XDD11LM"],
        # Ceiling Light MX650 (Color Temp adjustable)
        "lumi.light.cwopcn02": ["Aqara", "Opple MX650", "XDD12LM"],
        # Ceiling Light MX480 (Color Temp adjustable)
        "lumi.light.cwopcn03": ["Aqara", "Opple MX480", "XDD13LM"],
        # AqaraSmartDimmer ModuleT1（0-10v）
        "lumi.light.cwacn1": ["Aqara", "0-10V Dimmer", "ZNTGMK12LM"],
        # Spotlight (Color Temp adjustable)
        "lumi.light.cwjwcn01": ["Aqara", "Spotlight", ""],
        # Downlight (Color Temp adjustable)
        "lumi.light.cwjwcn02": ["Aqara", "Spotlight", ""],
        # Aqara Dual Color Temp Driver T1 Pro
        "lumi.light.acn004": ["Aqara", "Double Color Temp Driver T1 Pro", ""],
        # Track Light H1 Pro
        "lumi.light.acn006": ["Aqara", "Rail Light H1 Pro", ""],
        # Spotlight T2 (15 Degrees)
        "lumi.light.acn023": ["Aqara", "Spotlight T2", ""],
        # Spotlight T2 (24 Degrees)
        "lumi.light.acn024": ["Aqara", "Spotlight T2", ""],
        # Spotlight T2 (36 Degrees)
        "lumi.light.acn025": ["Aqara", "Spotlight T2", ""],
        # Downlight T2 (60 Degrees)
        "lumi.light.acn026": ["Aqara", "Spotlight T2", ""],
        # Spotlight/Downlight T3
        "lumi.light.acn128": ["Aqara", "Spotlight T3", ""],
        "params": [
            {
                "light": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "light",
                        "supported_features": LightEntityFeature.EFFECT,
                        "supported_color_modes": {
                            ColorMode.COLOR_TEMP,
                        },
                        "color_mode": ColorMode.COLOR_TEMP,
                        "min_color_temp_kelvin": 2703,
                        "max_color_temp_kelvin": 6500,
                    },
                    MK_RESOURCES: {
                        "toggle": ("4.1.85", "_attr_is_on"),
                        "brightness": ("14.1.85", "_attr_brightness"),
                        "color_temp_kelvin": ("14.2.85", "_attr_color_temp_kelvin"),
                        "zigbee_lqi": ("8.0.2007", "_attr_zigbee_lqi"),
                    },
                }
            }
        ],
    },
    {
        # Aqara LED Bulb T1
        "lumi.light.cwac02": ["Aqara", "Bulb T1", "ZNLDP13LM"],
        # LED Bulb T1 (Color Temp adjustable)
        "lumi.light.acn014": ["Aqara", "Bulb T1", ""],
        # Aqara Ceiling Light L1-350
        "lumi.light.acn003": ["Aqara", "Light L1-350", ""],
        # AqaraSkylight H1
        "lumi.light.acn015": ["Aqara", "Light H1", ""],
        "params": [
            {
                "light": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "light",
                        "supported_features": LightEntityFeature.EFFECT,
                        "supported_color_modes": {
                            ColorMode.COLOR_TEMP,
                        },
                        "color_mode": ColorMode.COLOR_TEMP,
                        "min_color_temp_kelvin": 2703,
                        "max_color_temp_kelvin": 6500,
                    },
                    MK_RESOURCES: {
                        "toggle": ("4.1.85", "_attr_is_on"),
                        "brightness": ("1.7.85", "_attr_brightness"),
                        "color_temp_kelvin": ("1.9.85", "_attr_color_temp_kelvin"),
                        "zigbee_lqi": ("8.0.2007", "_attr_zigbee_lqi"),
                    },
                }
            }
        ],
    },
    {
        # Ambient Ceiling Light T1 (40W)
        "lumi.light.acn032": ["Aqara", "Ceiling Light T1", ""],
        "params": [
            {
                "light": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "light",
                        "supported_features": LightEntityFeature.EFFECT,
                        "supported_color_modes": {
                            ColorMode.COLOR_TEMP,
                        },
                        "color_mode": ColorMode.COLOR_TEMP,
                        "min_color_temp_kelvin": 2703,
                        "max_color_temp_kelvin": 6500,
                        "unique_id_extra": "ch1",
                    },
                    MK_RESOURCES: {
                        "toggle": ("4.1.85", "_attr_is_on"),
                        "brightness": ("1.7.85", "_attr_brightness"),
                        "color_temp_kelvin": ("1.9.85", "_attr_color_temp_kelvin"),
                    },
                }
            },
            {
                "light": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "light",
                        "supported_features": LightEntityFeature.EFFECT,
                        "supported_color_modes": {
                            ColorMode.COLOR_TEMP,
                        },
                        "color_mode": ColorMode.COLOR_TEMP,
                        "min_color_temp_kelvin": 2703,
                        "max_color_temp_kelvin": 6500,
                        "unique_id_extra": "ch2",
                    },
                    MK_RESOURCES: {
                        "toggle": ("4.2.85", "_attr_is_on"),
                        "brightness": ("1.8.85", "_attr_brightness"),
                        "color_temp_kelvin": ("1.10.85", "_attr_color_temp_kelvin"),
                    },
                }
            },
        ],
    },
    {
        # Smart LED Strip Driver T1 (60W/120W/240W)
        "lumi.dimmer.acn003": ["Aqara", "LED Strip Dimmer T1", "ZNDDQDQ11LM"],
        "lumi.dimmer.acn004": ["Aqara", "LED Strip Dimmer T1", "ZNDDQDQ12LM"],
        "lumi.dimmer.acn005": ["Aqara", "LED Strip Dimmer T1", "ZNDDQDQ13LM"],
        "params": [
            {
                "light": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "light",
                        "supported_features": LightEntityFeature.EFFECT,
                        "supported_color_modes": {
                            ColorMode.COLOR_TEMP,
                        },
                        "color_mode": ColorMode.COLOR_TEMP,
                        "min_color_temp_kelvin": 2700,
                        "max_color_temp_kelvin": 6500,
                    },
                    MK_RESOURCES: {
                        "toggle": ("4.1.85", "_attr_is_on"),
                        "brightness": ("1.7.85", "_attr_brightness"),
                        "color_temp_kelvin": ("1.9.85", "_attr_color_temp_kelvin"),
                    },
                }
            }
        ],
    },
    # RGB type
    {
        # AqaraSmartDimmer Module T1
        "lumi.light.rgbac1": ["Aqara", "RGBW LED Controller T1", "ZNTGMK11LM"],
        # AqaraSmartLED Strip Driver Module
        "lumi.dimmer.rcbac1": ["Aqara", "RGBW LED Dimmer", "ZNDDMK11LM"],
        "params": [
            {
                "light": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "light",
                        "supported_features": LightEntityFeature.EFFECT,
                        "supported_color_modes": {
                            ColorMode.XY,
                        },
                        "color_mode": ColorMode.XY,
                    },
                    MK_RESOURCES: {
                        "toggle": ("4.1.85", "_attr_is_on"),
                        "brightness": ("14.1.85", "_attr_brightness"),
                        "color": ("14.8.85", "_attr_xy_color"),
                        "color_temp_kelvin": ("14.2.85", "_attr_color_temp_kelvin"),
                        "zigbee_lqi": ("8.0.2007", "_attr_zigbee_lqi"),
                    },
                }
            }
        ],
    },
    {
        # LED Strip T1
        "lumi.light.acn132": ["Aqara", "RGB LED Belt T1", ""],
        "params": [
            {
                "light": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "light",
                        "supported_features": LightEntityFeature.EFFECT,
                        "supported_color_modes": {
                            ColorMode.XY,
                        },
                        "color_mode": ColorMode.XY,
                    },
                    MK_RESOURCES: {
                        "toggle": ("4.1.85", "_attr_is_on"),
                        "brightness": ("1.7.85", "_attr_brightness"),
                        "color": ("14.8.85", "_attr_xy_color"),
                        "zigbee_lqi": ("8.0.2007", "_attr_zigbee_lqi"),
                    },
                }
            }
        ],
    },
    ##################################Curtain##################################
    {
        # SmartCurtain Motor (ZigbeeCurtain version)
        "lumi.curtain.v1": ["Aqara", "Curtain Motor Zigbee", ""],
        # AqaraSmartCurtain Motor T1
        "lumi.curtain.acn007": ["Aqara", "Curtain Motor T1", ""],
        # SmartCurtain Motor C2
        "lumi.curtain.hagl07": ["Aqara", "Curtain Motor C2", ""],
        # AqaraSmartCurtain MotorA1
        "lumi.curtain.hagl08": ["Aqara", "Curtain Motor A1", ""],
        # SmartCurtain Motor B1
        "lumi.curtain.hagl04": ["Aqara", "Curtain Motor B1", ""],
        # AqaraSmartCurtain Motor T2
        "lumi.curtain.acn015": ["Aqara", "Curtain Motor T2", ""],
        # Smart Tubular Motor
        "lumi.curtain.aq2": ["Aqara", "Tube Motor", ""],
        # Smart Tubular Motor T1
        "lumi.curtain.vagl02": ["Aqara", "Tube Motor T1", ""],
        "params": [
            {
                "cover": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "curtain",
                        "device_class": CoverDeviceClass.CURTAIN,
                        "state_class": CoverState,
                        "supported_features": CoverEntityFeature.OPEN
                        | CoverEntityFeature.CLOSE
                        | CoverEntityFeature.STOP
                        | CoverEntityFeature.SET_POSITION,
                    },
                    MK_RESOURCES: {
                        "is_closed": ("14.2.85", "_attr_is_closed"),
                        "current_cover_position": (
                            "1.1.85",
                            "_attr_current_cover_position",
                        ),
                        "running_status": ("14.4.85", "_attr_native_value"),
                        "zigbee_lqi": ("8.0.2007", "_attr_zigbee_lqi"),
                    },
                }
            }
        ],
    },
    {
        # SmartCurtain Motor B1
        "lumi.curtain.hagl04": ["Aqara", "Curtain Motor B1", ""],
        "params": [
            {
                "cover": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "curtain",
                        "device_class": CoverDeviceClass.CURTAIN,
                        "state_class": CoverState,
                        "supported_features": CoverEntityFeature.OPEN
                        | CoverEntityFeature.CLOSE
                        | CoverEntityFeature.STOP
                        | CoverEntityFeature.SET_POSITION,
                    },
                    MK_RESOURCES: {
                        "is_closed": ("14.2.85", "_attr_is_closed"),
                        "current_cover_position": (
                            "1.1.85",
                            "_attr_current_cover_position",
                        ),
                        "running_status": ("14.4.85", "_attr_native_value"),
                        "zigbee_lqi": ("8.0.2007", "_attr_zigbee_lqi"),
                    },
                }
            },
            {
                "sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "battery",
                        "device_class": SensorDeviceClass.BATTERY,
                        "state_class": SensorStateClass.MEASUREMENT,
                        "unit_of_measurement": PERCENTAGE,
                    },
                    MK_RESOURCES: {"battery": ("8.0.2001", "_attr_native_value")},
                }
            },
        ],
    },
    {
        # AqaraSmartCurtain Motor C3
        "lumi.curtain.acn04": ["Aqara", "Curtain Motor C3", ""],
        "params": [
            {
                "cover": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "curtain",
                        "device_class": CoverDeviceClass.CURTAIN,
                        "state_class": CoverState,
                        "supported_features": CoverEntityFeature.OPEN
                        | CoverEntityFeature.CLOSE
                        | CoverEntityFeature.STOP
                        | CoverEntityFeature.SET_POSITION,
                    },
                    MK_RESOURCES: {
                        "is_closed": ("14.2.85", "_attr_is_closed"),
                        "current_cover_position": (
                            "1.1.85",
                            "_attr_current_cover_position",
                        ),
                        "running_status": ("13.4.85", "_attr_native_value"),
                        "zigbee_lqi": ("8.0.2007", "_attr_zigbee_lqi"),
                    },
                }
            }
        ],
    },
    {
        # SmartCurtain CompanionE1
        "lumi.curtain.acn003": ["Aqara", "Curtain Partner E1", ""],
        "params": [
            {
                "cover": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "curtain",
                        "device_class": CoverDeviceClass.CURTAIN,
                        "state_class": CoverState,
                        "supported_features": CoverEntityFeature.OPEN
                        | CoverEntityFeature.CLOSE
                        | CoverEntityFeature.STOP
                        | CoverEntityFeature.SET_POSITION,
                    },
                    MK_RESOURCES: {
                        "is_closed": ("14.8.85", "_attr_is_closed"),
                        "current_cover_position": (
                            "1.1.85",
                            "_attr_current_cover_position",
                        ),
                        "running_status": ("14.4.85", "_attr_native_value"),
                    },
                }
            },
            {
                "sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "battery",
                        "device_class": SensorDeviceClass.BATTERY,
                        "state_class": SensorStateClass.MEASUREMENT,
                        "unit_of_measurement": PERCENTAGE,
                    },
                    MK_RESOURCES: {"battery": ("8.0.2001", "_attr_native_value")},
                }
            },
        ],
    },
    {
        # SmartRoller Shade CompanionE1
        "lumi.curtain.acn002": ["Aqara", "Curtain Partner E1", ""],
        "params": [
            {
                "cover": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "curtain",
                        "device_class": CoverDeviceClass.CURTAIN,
                        "state_class": CoverState,
                        "supported_features": CoverEntityFeature.OPEN
                        | CoverEntityFeature.CLOSE
                        | CoverEntityFeature.STOP
                        | CoverEntityFeature.SET_POSITION,
                    },
                    MK_RESOURCES: {
                        "is_closed": ("14.8.85", "_attr_is_closed"),
                        "current_cover_position": (
                            "1.1.85",
                            "_attr_current_cover_position",
                        ),
                        "running_status": ("14.4.85", "_attr_native_value"),
                    },
                }
            },
        ],
    },
    ##################################Clothes Dryer##################################
    {
        # Smart Clothes Dryer H1
        "lumi.airer.acn001": ["Aqara", "Airer H1", ""],
        "params": [
            {
                "cover": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "airer",
                        "device_class": CoverDeviceClass.AWNING,
                        "state_class": CoverState,
                        "supported_features": CoverEntityFeature.OPEN
                        | CoverEntityFeature.CLOSE
                        | CoverEntityFeature.STOP,
                    },
                    MK_RESOURCES: {
                        "is_closed": ("14.1.85", "_attr_is_closed"),
                    },
                }
            },
            {
                "switch": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "switch",
                        "unique_id_extra": "1",
                    },
                    MK_RESOURCES: {
                        "toggle": ("4.21.85", "_attr_is_on"),
                    },
                }
            },
            {
                "switch": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "switch",
                        "entity_name": "Air Dry",
                        "unique_id_extra": "2",
                    },
                    MK_RESOURCES: {
                        "toggle": ("4.66.85", "_attr_is_on"),
                    },
                }
            },
            {
                "switch": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "switch",
                        "entity_name": "Dry",
                        "unique_id_extra": "3",
                    },
                    MK_RESOURCES: {
                        "toggle": ("4.67.85", "_attr_is_on"),
                    },
                }
            },
            {
                "switch": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "switch",
                        "entity_name": "Disinfect",
                        "unique_id_extra": "4",
                    },
                    MK_RESOURCES: {
                        "toggle": ("4.22.85", "_attr_is_on"),
                    },
                }
            },
        ],
    },
    {
        # Aqara Smart Clothes Dryer Lite
        "lumi.airer.acn02": ["Aqara", "Airer Lite", ""],
        "params": [
            {
                "cover": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "airer",
                        "device_class": CoverDeviceClass.AWNING,
                        "state_class": CoverState,
                        "supported_features": CoverEntityFeature.OPEN
                        | CoverEntityFeature.CLOSE
                        | CoverEntityFeature.STOP
                        | CoverEntityFeature.SET_POSITION,
                    },
                    MK_RESOURCES: {
                        "is_closed": ("14.1.85", "_attr_is_closed"),
                        "current_cover_position": (
                            "1.1.85",
                            "_attr_current_cover_position",
                        ),
                    },
                }
            },
            {
                "switch": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "switch",
                    },
                    MK_RESOURCES: {
                        "toggle": ("14.2.85", "_attr_is_on"),
                    },
                }
            },
        ],
    },
    ##################################Wireless Switch##################################
    {
        # Wireless Switch（WirelessSingle Key version）
        "lumi.remote.b186acn01": ["Aqara", "Single Wall Button", "WXKG03LM"],
        # Wireless SwitchT1
        "lumi.remote.b1acn02": [
            "Aqara",
            "Wireless Remote Switch T1 (Single Rocker)",
            "",
        ],
        # Wireless Switch
        "lumi.remote.b1acn01": ["Aqara", "Wireless Remote Switch (Single Rocker)", ""],
        # Wireless Switch
        "lumi.sensor_switch.v1": [
            "Aqara",
            "Wireless Remote Switch (Single Rocker)",
            "",
        ],
        # Wireless Switch
        "lumi.sensor_switch.v2": [
            "Aqara",
            "Wireless Remote Switch (Single Rocker)",
            "",
        ],
        # Wireless Switch
        "lumi.sensor_switch.aq2": [
            "Aqara",
            "Wireless Remote Switch (Single Rocker)",
            "",
        ],
        # Wireless Switch（Enhanced version）
        "lumi.sensor_switch.aq3": [
            "Aqara",
            "Wireless Remote Switch Plus (Single Rocker)",
            "",
        ],
        # Wireless SwitchH1（WirelessSingle Key version）
        "lumi.remote.b18ac1": [
            "Aqara",
            "Wireless Remote Switch H1 (Single Rocker)",
            "WXKG14LM",
        ],
        # Wireless SwitchE1（WirelessSingle Key version）
        "lumi.remote.acn003": [
            "Aqara",
            "Wireless Remote Switch E1 (Single Rocker)",
            "",
        ],
        # Wireless SwitchE1（WirelessSingle Key version）
        "lumi.remote.acn007": [
            "Aqara",
            "Wireless Remote Switch E1 (Single Rocker)",
            "WXKG16LM",
        ],
        # Wireless SwitchD1（WirelessSingle Key version）
        "lumi.remote.b186acn02": [
            "Aqara",
            "Wireless Remote Switch D1 (Single Rocker)",
            "WXKG06LM",
        ],
        # Wireless SwitchT1（WirelessSingle Key version）
        "lumi.remote.b186acn03": [
            "Aqara",
            "Wireless Remote Switch T1 (Single Rocker)",
            "",
        ],
        "params": [
            {
                "event": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "button",
                        "device_class": EventDeviceClass.BUTTON,
                    },
                    MK_RESOURCES: {"button": ("13.1.85", "_attr_trigger")},
                }
            }
        ],
    },
    ###Wireless 2-Key
    {
        # Wireless Scene Switch（Double Keys version）
        "lumi.remote.b286acn01": ["Aqara", "Double Wall Button", "WXKG02LM"],
        # Wireless SwitchH1（WirelessDouble Keys version）
        "lumi.remote.b28ac1": [
            "Aqara",
            "Wireless Remote Switch H1 (Double Rocker)",
            "WXKG15LM",
        ],
        # Wireless SwitchE1（WirelessDouble Keys version）
        "lumi.remote.acn004": [
            "Aqara",
            "Wireless Remote Switch E1 (Double Rocker)",
            "WXKG17LM",
        ],
        # Wireless SwitchD1（WirelessDouble Keys version）
        "lumi.remote.b286acn02": [
            "Aqara",
            "Wireless Remote Switch D1 (Double Rocker)",
            "WXKG07LM",
        ],
        # Wireless SwitchT1（WirelessDouble Keys version）
        "lumi.remote.b286acn03": [
            "Aqara",
            "Wireless Remote Switch T1 (Double Rocker)",
            "",
        ],
        "params": [
            {
                "event": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "button",
                        "device_class": EventDeviceClass.BUTTON,
                    },
                    MK_RESOURCES: {"button": ("13.{}.85", "_attr_trigger")},
                    MK_MAPPING_PARAMS: {"ch_count": 2},
                }
            }
        ],
    },
    ###Wireless 4-Key
    {
        # Wireless Scene Switch（Quadruple Keys version）
        "lumi.remote.b486opcn01": ["Aqara", "Wireless Remote Switch (Four Rocker)", ""],
        "params": [
            {
                "event": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "button",
                        "device_class": EventDeviceClass.BUTTON,
                    },
                    MK_RESOURCES: {"button": ("13.{}.85", "_attr_trigger")},
                    MK_MAPPING_PARAMS: {"ch_count": 4},
                }
            }
        ],
    },
    ###Wireless 6-Key
    {
        # Wireless Switch（6-Key version）
        "lumi.remote.b686opcn01": ["Aqara", "Wireless Remote Switch (Six Rocker)", ""],
        "params": [
            {
                "event": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "button",
                        "device_class": EventDeviceClass.BUTTON,
                    },
                    MK_RESOURCES: {"button": ("13.{}.85", "_attr_trigger")},
                    MK_MAPPING_PARAMS: {"ch_count": 6},
                }
            }
        ],
    },
    ###Wireless Knob
    {
        # Smart Knob Switch H1 (Wireless version)
        "lumi.remote.rkba01": ["Aqara", "Wireless rotary switch H1", ""],
        "params": [
            {
                "event": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "button",
                        "device_class": EventDeviceClass.BUTTON,
                    },
                    MK_RESOURCES: {"button": ("13.1.85", "_attr_trigger")},
                }
            },
            {
                "sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "rotation_angle",
                        "device_class": "",
                        "state_class": SensorStateClass.MEASUREMENT,
                        "unit_of_measurement": "°",
                    },
                    MK_RESOURCES: {"state": ("0.22.85", "_attr_native_value")},
                }
            },
            {
                "sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "press_rotation_angle",
                        "device_class": "",
                        "state_class": SensorStateClass.MEASUREMENT,
                        "unit_of_measurement": "°",
                    },
                    MK_RESOURCES: {"state": ("0.29.85", "_attr_native_value")},
                }
            },
        ],
    },
    ###############################Sensor###########################################
    ###Temp/Humidity
    {
        # Xiaomi Temp & Humidity Sensor
        "lumi.sensor_ht.v1": ["Xiaomi", "TH Sensor", "WSDCGQ01LM"],
        # Temp/Humidity Sensor T1
        "lumi.sensor_ht.agl02": ["Aqara", "T1 TH Sensor", ""],
        # Temp/Humidity Sensor
        "lumi.weather.v1": ["Aqara", "TH Sensor", "WSDCGQ11LM"],
        "params": [
            {
                "sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "temperature",
                        "device_class": SensorDeviceClass.TEMPERATURE,
                        "state_class": SensorStateClass.MEASUREMENT,
                        "unit_of_measurement": UnitOfTemperature.CELSIUS,
                    },
                    MK_RESOURCES: {"temperature": ("0.1.85", "_attr_native_value")},
                }
            },
            {
                "sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "humidity",
                        "device_class": SensorDeviceClass.HUMIDITY,
                        "state_class": SensorStateClass.MEASUREMENT,
                        "unit_of_measurement": PERCENTAGE,
                    },
                    MK_RESOURCES: {"humidity": ("0.2.85", "_attr_native_value")},
                }
            },
        ],
    },
    ### Air Quality
    {
        # TVOC Air Quality Monitor
        "lumi.airmonitor.acn01": ["Aqara", "TVOC Sensor", ""],
        "params": [
            {
                "sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "temperature",
                        "device_class": SensorDeviceClass.TEMPERATURE,
                        "state_class": SensorStateClass.MEASUREMENT,
                        "unit_of_measurement": UnitOfTemperature.CELSIUS,
                    },
                    MK_RESOURCES: {"temperature": ("0.1.85", "_attr_native_value")},
                }
            },
            {
                "sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "humidity",
                        "device_class": SensorDeviceClass.HUMIDITY,
                        "state_class": SensorStateClass.MEASUREMENT,
                        "unit_of_measurement": PERCENTAGE,
                    },
                    MK_RESOURCES: {"humidity": ("0.2.85", "_attr_native_value")},
                }
            },
            {
                "sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "TVOC",
                        "device_class": SensorDeviceClass.VOLATILE_ORGANIC_COMPOUNDS_PARTS,
                        "state_class": SensorStateClass.MEASUREMENT,
                        "unit_of_measurement": CONCENTRATION_PARTS_PER_BILLION,
                    },
                    MK_RESOURCES: {
                        "TVOC": (
                            "0.3.85",
                            "_attr_native_value",
                        )
                    },
                }
            },
        ],
    },
    ###Illuminance Sensor
    {
        # Illuminance Sensor T1
        "lumi.sen_ill.agl01": ["Aqara", "Light Sensor T1", ""],
        "params": [
            {
                "sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "illuminance",
                        "device_class": SensorDeviceClass.ILLUMINANCE,
                        "state_class": SensorStateClass.MEASUREMENT,
                        "unit_of_measurement": LIGHT_LUX,
                    },
                    MK_RESOURCES: {"illuminance": ("0.3.85", "_attr_native_value")},
                }
            },
            {
                "sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "battery",
                        "device_class": SensorDeviceClass.BATTERY,
                        "state_class": SensorStateClass.MEASUREMENT,
                        "unit_of_measurement": PERCENTAGE,
                    },
                    MK_RESOURCES: {"battery": ("8.0.2001", "_attr_native_value")},
                }
            },
        ],
    },
    ###Presence Sensor
    {
        # Presence Sensor
        "lumi.sensor_motion.v1": ["Xiaomi", "Motion Sensor", "RTCGQ01LM"],
        "lumi.sensor_motion.v2": ["Xiaomi", "Motion Sensor", "RTCGQ01LM"],
        # Presence Sensor P1
        "lumi.motion.ac02": ["Aqara", "Motion Sensor P1", ""],
        # Presence Sensor E1
        "lumi.motion.acn001": ["Aqara", "Motion Sensor E1", ""],
        "params": [
            {
                "binary_sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "motion",
                        "device_class": BinarySensorDeviceClass.MOTION,
                    },
                    MK_RESOURCES: {
                        "motion": ("3.1.85", "_attr_native_value"),
                        "zigbee_lqi": ("8.0.2007", "_attr_zigbee_lqi"),
                    },
                }
            }
        ],
    },
    {
        # Presence Sensor with Brightness
        "lumi.sensor_motion.aq2": ["Aqara", "Motion Sensor", "RTCGQ11LM"],
        # Presence Sensor T1
        "lumi.motion.agl02": ["Aqara", "Motion Sensor T1", ""],
        "params": [
            {
                "binary_sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "motion",
                        "device_class": BinarySensorDeviceClass.MOTION,
                    },
                    MK_RESOURCES: {
                        "motion": ("3.1.85", "_attr_native_value"),
                        "zigbee_lqi": ("8.0.2007", "_attr_zigbee_lqi"),
                        "voltage": ("8.0.2008", "_attr_voltage"),
                    },
                }
            },
            {
                "sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "illuminance",
                        "device_class": SensorDeviceClass.ILLUMINANCE,
                        "state_class": SensorStateClass.MEASUREMENT,
                        "unit_of_measurement": LIGHT_LUX,
                        "entity_name": "Illuminance",
                    },
                    MK_RESOURCES: {"illumination": ("0.3.85", "_attr_native_value")},
                }
            },
        ],
    },
    ###High Precision Presence Sensor
    {
        # High Precision Presence Sensor
        "lumi.motion.agl04": ["Aqara", "Precision Motion Sensor", "RTCGQ13LM"],
        "params": [
            {
                "binary_sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "motion",
                        "device_class": BinarySensorDeviceClass.MOTION,
                    },
                    MK_RESOURCES: {
                        "motion": ("3.1.85", "_attr_native_value"),
                        "detect_time": ("8.0.2115", "_attr_detect_time"),
                        "zigbee_lqi": ("8.0.2007", "_attr_zigbee_lqi"),
                        "voltage": ("8.0.2008", "_attr_voltage"),
                    },
                }
            },
        ],
    },
    ###PresenceSensor
    {
        # Presence
        "lumi.motion.ac01": ["Aqara", "Presence Sensor FP1", "RTCZCGQ11LM"],
        # AI Presence Sensor FP1E
        "lumi.sensor_occupy.agl1": ["Aqara", "Presence Sensor FP1E", ""],
        "params": [
            {
                "binary_sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "default",
                        "device_class": BinarySensorDeviceClass.MOTION,
                    },
                    MK_RESOURCES: {
                        "exist": ("3.51.85", "_attr_is_on"),
                    },
                }
            },
            {
                "event": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "default",
                        "event_mapping": FP_MOTION_MAPPING,
                        "entity_name": "Motion Detection Event",
                    },
                    MK_RESOURCES: {
                        "event": ("13.27.85", "_attr_native_value"),
                    },
                }
            },
        ],
    },
    {
        # Presence Sensor FP2
        "lumi.motion.agl001": ["Aqara", "Presence Sensor FP2", ""],
        "params": [
            {
                "binary_sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "default",
                        "device_class": BinarySensorDeviceClass.MOTION,
                        "entity_name": "Area",
                    },
                    MK_RESOURCES: {
                        "exist": ("3.{}.85", "_attr_is_on"),
                    },
                }
            },
            {
                "binary_sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "default",
                        "device_class": BinarySensorDeviceClass.MOTION,
                        "entity_name": "All Area",
                    },
                    MK_RESOURCES: {
                        "exist": ("3.51.85", "_attr_is_on"),
                    },
                    MK_MAPPING_PARAMS: {"ch_count": None},
                }
            },
            {
                "sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "illuminance",
                        "device_class": SensorDeviceClass.ILLUMINANCE,
                        "state_class": SensorStateClass.MEASUREMENT,
                        "unit_of_measurement": LIGHT_LUX,
                        "entity_name": "Illuminance",
                    },
                    MK_RESOURCES: {"illumination": ("0.4.85", "_attr_native_value")},
                    MK_MAPPING_PARAMS: {"ch_count": None},
                }
            },
        ],
    },
    ###Contact Sensor
    {
        # Contact Sensor
        "lumi.sensor_magnet.v1": ["Xiaomi", "Door Sensor", "MCCGQ01LM"],
        "lumi.sensor_magnet.v2": ["Xiaomi", "Door Sensor", "MCCGQ01LM"],
        "lumi.sensor_magnet.aq2": ["Aqara", "Door Sensor", "MCCGQ11LM"],
        # Contact SensorT1
        "lumi.magnet.agl02": ["Aqara", "Door Sensor T1", "MCCGQ12LM"],
        # Contact SensorE1
        "lumi.magnet.acn001": ["Aqara", "Door Sensor E1", "MCCGQ14LM"],
        # Contact SensorP1
        "lumi.magnet.ac01": ["Aqara", "Door Sensor P1", "MCCGQ13LM"],
        "params": [
            {
                "binary_sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "contact",
                        "device_class": BinarySensorDeviceClass.DOOR,
                    },
                    MK_RESOURCES: {
                        "status": ("3.1.85", "_attr_native_value"),
                        "zigbee_lqi": ("8.0.2007", "_attr_zigbee_lqi"),
                        "voltage": ("8.0.2008", "_attr_voltage"),
                    },
                }
            }
        ],
    },
    ###Water Leak Sensor
    {
        # Water Leak Sensor
        "lumi.sensor_wleak.aq1": ["Aqara", "Water Leak Sensor", "SJCGQ11LM"],
        "lumi.sensor_wleak.v1": ["Aqara", "Water Leak Sensor", ""],
        "lumi.flood.agl02": ["Aqara", "Water Leak Sensor T1", "SJCGQ12LM"],
        "lumi.flood.acn001": ["Aqara", "Water Leak Sensor E1", "SJCGQ13LM"],
        "params": [
            {
                "binary_sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "moisture",
                        "device_class": BinarySensorDeviceClass.MOISTURE,
                    },
                    MK_RESOURCES: {
                        "moisture": ("3.1.85", "_attr_is_on"),
                        "zigbee_lqi": ("8.0.2007", "_attr_zigbee_lqi"),
                        "voltage": ("8.0.2008", "_attr_voltage"),
                    },
                }
            }
        ],
    },
    ###Smoke Sensor
    {
        # Xiaomi Smoke Alarm
        "lumi.sensor_smoke.v1": ["Xiaomi", "Smoke Sensor", "JTYJ-GD-01LM/BW"],
        "lumi.sensor_smoke.acn03": ["Xiaomi", "Smoke Sensor", ""],
        "params": [
            {
                "binary_sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "smoke",
                        "device_class": BinarySensorDeviceClass.SMOKE,
                    },
                    MK_RESOURCES: {"smoke": ("13.1.85", "_attr_is_on")},
                }
            },
        ],
    },
    ###Natural Gas Sensor
    {
        # Natural Gas Alarm
        "lumi.sensor_natgas.v1": ["Aqara", "Gas Alarm", ""],
        "params": [
            {
                "binary_sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "gas",
                        "device_class": BinarySensorDeviceClass.GAS,
                    },
                    MK_RESOURCES: {"gas": ("13.1.85", "_attr_is_on")},
                }
            },
        ],
    },
    {
        # AqaraNatural Gas Alarm
        "lumi.sensor_gas.acn02": ["Aqara", "Gas Sensor", ""],
        "params": [
            {
                "sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "gas",
                        "device_class": SensorDeviceClass.GAS,
                        "state_class": SensorStateClass.MEASUREMENT,
                        "unit_of_measurement": "",
                    },
                    MK_RESOURCES: {"density": ("0.5.85", "_attr_native_value")},
                }
            },
        ],
    },
    ###############################Door Lock#############################################
    {
        # P100Door Lock
        "aqara.lock.wbzac1": ["Aqara", "DoorLock P100", ""],
        "params": [
            {
                "binary_sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "contact",
                        "device_class": BinarySensorDeviceClass.DOOR,
                    },
                    MK_RESOURCES: {
                        "status": ("13.12.85", "_attr_native_value"),
                    },
                }
            },
            {
                "sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "contact",
                        "device_class": "",
                        "state_class": "",
                        "unit_of_measurement": "",
                    },
                    MK_RESOURCES: {"status": ("13.2.85", "_attr_native_value")},
                }
            },
        ],
    },
    #################################Climate、Floor Heating####################################
    {
        # AC Companion P3
        "lumi.aircondition.acn05": ["Aqara", "AC Partner P3", ""],
        "params": [
            {
                "climate": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "ac_partner_p3",
                        "supported_features": ClimateEntityFeature.TARGET_TEMPERATURE
                        | ClimateEntityFeature.TARGET_TEMPERATURE_RANGE
                        | ClimateEntityFeature.FAN_MODE
                        | ClimateEntityFeature.PRESET_MODE
                        | ClimateEntityFeature.SWING_MODE
                        | ClimateEntityFeature.TURN_ON
                        | ClimateEntityFeature.TURN_OFF,
                        "max_temp": float(30),
                        "min_temp": float(16),
                        "hvac_modes": [
                            HVACMode.OFF,
                            HVACMode.HEAT,
                            HVACMode.COOL,
                            HVACMode.AUTO,
                            HVACMode.DRY,
                            HVACMode.FAN_ONLY,
                        ],
                        "fan_modes": [
                            FAN_AUTO,
                            FAN_LOW,
                            FAN_MEDIUM,
                            FAN_HIGH,
                        ],
                        "swing_modes": [
                            SWING_OFF,
                            SWING_ON,
                        ],
                        "preset_modes": [PRESET_NONE, PRESET_BOOST],
                        "temperature_unit": UnitOfTemperature.CELSIUS,
                        "target_temperature_step": float(1),
                    },
                    MK_RESOURCES: {
                        "ac_fun_ctl": ("8.0.2116", "_attr_native_value"),
                        "ac_quick_cool": ("4.4.85", "_attr_native_value"),
                        "ac_zip_mode": ("14.32.85", "_attr_native_value"),
                        "ac_on_off": ("3.1.85", "_attr_native_value"),
                    },
                }
            },
            {
                "switch": {
                    MK_INIT_PARAMS: {MK_HASS_NAME: "switch"},
                    MK_RESOURCES: {
                        "toggle": ("4.1.85", "_attr_is_on"),
                    },
                }
            },
            {
                "sensor": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "power",
                        "device_class": SensorDeviceClass.POWER,
                        "state_class": SensorStateClass.MEASUREMENT,
                        "unit_of_measurement": UnitOfPower.WATT,
                    },
                    MK_RESOURCES: {"power": ("0.11.85", "_attr_native_value")},
                }
            },
        ],
    },
    {
        # ClimateThermostat
        "lumi.ctrl_hvac.es1": ["Aqara", "AC Controller", ""],
        "params": [
            {
                "climate": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "airrtc_tcpecn02",
                        "supported_features": ClimateEntityFeature.TARGET_TEMPERATURE
                        | ClimateEntityFeature.TARGET_TEMPERATURE_RANGE
                        | ClimateEntityFeature.FAN_MODE
                        | ClimateEntityFeature.SWING_MODE
                        | ClimateEntityFeature.TURN_ON
                        | ClimateEntityFeature.TURN_OFF,
                        "max_temp": float(30),
                        "min_temp": float(16),
                        "hvac_modes": [
                            HVACMode.OFF,
                            HVACMode.HEAT,
                            HVACMode.COOL,
                            HVACMode.AUTO,
                            HVACMode.DRY,
                            HVACMode.FAN_ONLY,
                        ],
                        "fan_modes": [
                            FAN_AUTO,
                            FAN_LOW,
                            FAN_MEDIUM,
                            FAN_HIGH,
                        ],
                        "swing_modes": [
                            SWING_OFF,
                            SWING_ON,
                        ],
                        "temperature_unit": UnitOfTemperature.CELSIUS,
                        "target_temperature_step": float(1),
                    },
                    MK_RESOURCES: {
                        "ac_on_off": ("3.1.85", "_attr_native_value"),
                        "ac_state": ("14.2.85", "_attr_native_value"),
                    },
                }
            },
        ],
    },
    {
        # ClimateThermostat
        "lumi.airrtc.tcpecn01": ["Aqara", "AC Controller", ""],
        # ClimateThermostat S2
        "lumi.airrtc.tcpecn02": ["Aqara", "AC Controller S2", ""],
        # HVAC Thermostat (CO2)
        "lumi.airrtc.tcpco2ecn01": ["Aqara", "AC Controller CO2", ""],
        "params": [
            {
                "climate": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "airrtc_tcpecn02",
                        "supported_features": ClimateEntityFeature.TARGET_TEMPERATURE
                        | ClimateEntityFeature.TARGET_TEMPERATURE_RANGE
                        | ClimateEntityFeature.FAN_MODE
                        | ClimateEntityFeature.SWING_MODE
                        | ClimateEntityFeature.TURN_ON
                        | ClimateEntityFeature.TURN_OFF,
                        "max_temp": float(30),
                        "min_temp": float(16),
                        "hvac_modes": [
                            HVACMode.OFF,
                            HVACMode.HEAT,
                            HVACMode.COOL,
                            HVACMode.AUTO,
                            HVACMode.DRY,
                            HVACMode.FAN_ONLY,
                        ],
                        "fan_modes": [
                            FAN_AUTO,
                            FAN_LOW,
                            FAN_MEDIUM,
                            FAN_HIGH,
                        ],
                        "swing_modes": [
                            SWING_OFF,
                            SWING_ON,
                        ],
                        "temperature_unit": UnitOfTemperature.CELSIUS,
                        "target_temperature_step": float(1),
                    },
                    MK_RESOURCES: {
                        "ac_on_off": ("3.1.85", "_attr_native_value"),
                        "ac_state": ("14.2.85", "_attr_native_value"),
                        "current_temperature": ("3.2.85", "_attr_current_temperature"),
                    },
                }
            },
        ],
    },
    {
        # AC Companion (Enhanced version)
        "lumi.acpartner.v3": ["Aqara", "AC Partner V3", ""],
        "params": [
            {
                "climate": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "airrtc_tcpecn02",
                        "supported_features": ClimateEntityFeature.TARGET_TEMPERATURE
                        | ClimateEntityFeature.TARGET_TEMPERATURE_RANGE
                        | ClimateEntityFeature.FAN_MODE
                        | ClimateEntityFeature.SWING_MODE
                        | ClimateEntityFeature.TURN_ON
                        | ClimateEntityFeature.TURN_OFF,
                        "max_temp": float(30),
                        "min_temp": float(16),
                        "hvac_modes": [
                            HVACMode.OFF,
                            HVACMode.HEAT,
                            HVACMode.COOL,
                            HVACMode.AUTO,
                            HVACMode.DRY,
                            HVACMode.FAN_ONLY,
                        ],
                        "fan_modes": [
                            FAN_AUTO,
                            FAN_LOW,
                            FAN_MEDIUM,
                            FAN_HIGH,
                        ],
                        "swing_modes": [
                            SWING_OFF,
                            SWING_ON,
                        ],
                        "temperature_unit": UnitOfTemperature.CELSIUS,
                        "target_temperature_step": float(1),
                    },
                    MK_RESOURCES: {
                        "ac_on_off": ("3.1.85", "_attr_native_value"),
                        "ac_state": ("14.10.85", "_attr_native_value"),
                    },
                }
            },
            {
                "switch": {
                    MK_INIT_PARAMS: {MK_HASS_NAME: "switch"},
                    MK_RESOURCES: {
                        "toggle": ("4.1.85", "_attr_is_on"),
                    },
                }
            },
        ],
    },
    {
        # AC Companion
        "lumi.acpartner.aq1": ["Aqara", "AC Partner", ""],
        # AC Companion
        "lumi.acpartner.es1": ["Aqara", "AC Partner", ""],
        "params": [
            {
                "climate": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "airrtc_tcpecn02",
                        "supported_features": ClimateEntityFeature.TARGET_TEMPERATURE
                        | ClimateEntityFeature.TARGET_TEMPERATURE_RANGE
                        | ClimateEntityFeature.FAN_MODE
                        | ClimateEntityFeature.SWING_MODE
                        | ClimateEntityFeature.TURN_ON
                        | ClimateEntityFeature.TURN_OFF,
                        "max_temp": float(30),
                        "min_temp": float(16),
                        "hvac_modes": [
                            HVACMode.OFF,
                            HVACMode.HEAT,
                            HVACMode.COOL,
                            HVACMode.AUTO,
                            HVACMode.DRY,
                            HVACMode.FAN_ONLY,
                        ],
                        "fan_modes": [
                            FAN_AUTO,
                            FAN_LOW,
                            FAN_MEDIUM,
                            FAN_HIGH,
                        ],
                        "swing_modes": [
                            SWING_OFF,
                            SWING_ON,
                        ],
                        "temperature_unit": UnitOfTemperature.CELSIUS,
                        "target_temperature_step": float(1),
                    },
                    MK_RESOURCES: {
                        "ac_on_off": ("3.1.85", "_attr_native_value"),
                        "ac_state": ("14.10.85", "_attr_native_value"),
                    },
                }
            },
        ],
    },
    {
        # Thermostat Companion T1 (Indoor Unit)
        "aqara.airrtc.acn02": ["Aqara", "Thermostat Partner T1", ""],
        "params": [
            {
                "climate": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "airrtc_acn02",
                        "supported_features": ClimateEntityFeature.TARGET_TEMPERATURE
                        | ClimateEntityFeature.TARGET_TEMPERATURE_RANGE
                        | ClimateEntityFeature.FAN_MODE
                        | ClimateEntityFeature.TURN_ON
                        | ClimateEntityFeature.TURN_OFF,
                        "max_temp": float(30),
                        "min_temp": float(16),
                        "hvac_modes": [
                            HVACMode.OFF,
                            HVACMode.HEAT,
                            HVACMode.COOL,
                            HVACMode.AUTO,
                            HVACMode.DRY,
                            HVACMode.FAN_ONLY,
                        ],
                        "fan_modes": [
                            FAN_AUTO,
                            FAN_LOW,
                            FAN_MEDIUM,
                            FAN_HIGH,
                        ],
                        "temperature_unit": UnitOfTemperature.CELSIUS,
                        "target_temperature_step": float(1),
                    },
                    MK_RESOURCES: {
                        "ac_on_off": ("4.1.85", "_attr_native_value"),
                        "ac_temperature": ("1.1.85", "_attr_native_value"),
                        "ac_mode": ("14.140.85", "_attr_native_value"),
                        "ac_fan_mode": ("14.1.85", "_attr_native_value"),
                        "env_temperature": ("0.1.85", "_attr_native_value"),
                    },
                }
            },
        ],
    },
    {
        # Smart Thermostat S3
        "lumi.airrtc.pcacn2": ["Aqara", "Thermostat S3", ""],
        "lumi.airrtc.pcacn2_thermostat": ["Aqara", "Thermostat S3", ""],
        "params": [
            {
                "climate": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "airrtc_pcacn2",
                        "supported_features": ClimateEntityFeature.TARGET_TEMPERATURE
                        | ClimateEntityFeature.TARGET_TEMPERATURE_RANGE
                        | ClimateEntityFeature.FAN_MODE
                        | ClimateEntityFeature.TURN_ON
                        | ClimateEntityFeature.TURN_OFF,
                        "max_temp": float(30),
                        "min_temp": float(16),
                        "hvac_modes": [
                            HVACMode.OFF,
                            HVACMode.HEAT,
                            HVACMode.COOL,
                            HVACMode.FAN_ONLY,
                        ],
                        "fan_modes": [
                            FAN_AUTO,
                            FAN_LOW,
                            FAN_MEDIUM,
                            FAN_HIGH,
                        ],
                        "temperature_unit": UnitOfTemperature.CELSIUS,
                        "target_temperature_step": 0.5,
                    },
                    MK_RESOURCES: {
                        "ac_on_off": ("4.21.85", "_attr_native_value"),
                        "ac_temperature": ("1.8.85", "_attr_native_value"),
                        "ac_mode": ("14.51.85", "_attr_native_value"),
                        "ac_fan_mode": ("14.35.85", "_attr_native_value"),
                        "env_temperature": ("0.1.85", "_attr_native_value"),
                        "env_humidity": ("0.2.85", "_attr_native_value"),
                    },
                }
            },
        ],
    },
    {
        # Smart Valve Controller E1
        "lumi.airrtc.agl001": ["Aqara", "Valve Thermostat E1", ""],
        "params": [
            {
                "climate": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "airrtc_agl001",
                        "supported_features": ClimateEntityFeature.TARGET_TEMPERATURE
                        | ClimateEntityFeature.TARGET_TEMPERATURE_RANGE
                        | ClimateEntityFeature.TURN_ON
                        | ClimateEntityFeature.TURN_OFF,
                        "max_temp": float(30),
                        "min_temp": float(5),
                        "hvac_modes": [
                            HVACMode.OFF,
                            HVACMode.HEAT,
                        ],
                        "temperature_unit": UnitOfTemperature.CELSIUS,
                        "target_temperature_step": 0.5,
                    },
                    MK_RESOURCES: {
                        "ac_on_off": ("4.21.85", "_attr_native_value"),
                        "ac_temperature": ("1.8.85", "_attr_native_value"),
                        "ac_mode": ("14.51.85", "_attr_native_value"),
                        "env_temperature": ("0.1.85", "_attr_native_value"),
                    },
                }
            },
        ],
    },
    {
        # VRFAC Controller
        "lumi.airrtc.vrfegl01": ["Aqara", "VRF AC Controller", ""],
        "params": [
            {
                "climate": {
                    MK_INIT_PARAMS: {
                        MK_HASS_NAME: "airrtc_vrfegl01",
                        "supported_features": ClimateEntityFeature.TARGET_TEMPERATURE
                        | ClimateEntityFeature.TARGET_TEMPERATURE_RANGE
                        | ClimateEntityFeature.FAN_MODE
                        | ClimateEntityFeature.SWING_MODE
                        | ClimateEntityFeature.TURN_ON
                        | ClimateEntityFeature.TURN_OFF,
                        "max_temp": float(30),
                        "min_temp": float(16),
                        "hvac_modes": [
                            HVACMode.OFF,
                            HVACMode.HEAT,
                            HVACMode.COOL,
                            HVACMode.AUTO,
                            HVACMode.DRY,
                            HVACMode.FAN_ONLY,
                        ],
                        "fan_modes": [
                            FAN_AUTO,
                            FAN_LOW,
                            FAN_MEDIUM,
                            FAN_HIGH,
                        ],
                        "swing_modes": [
                            SWING_OFF,
                            SWING_ON,
                        ],
                        "temperature_unit": UnitOfTemperature.CELSIUS,
                        "target_temperature_step": float(1),
                    },
                    MK_RESOURCES: {
                        "ac_state": ("14.{}.85", "_attr_native_value"),
                    },
                }
            },
        ],
    },
    ##################################Unsupported devices##################################
    {
        "lumi.camera.acn005": ["Aqara", "DoorBell G4", ""],
        "params": [],
    },
]

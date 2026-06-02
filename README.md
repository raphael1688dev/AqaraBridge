# Aqara Bridge for Home Assistant

Based on the Aqara Open Platform, providing device control and subscription via cloud APIs.

[![version](https://img.shields.io/github/manifest-json/v/bernard3378/AqaraBridge?filename=custom_components%2Faqara_bridge%2Fmanifest.json)](https://github.com/bernard3378/AqaraBridge/releases/latest) [![stars](https://img.shields.io/github/stars/bernard3378/AqaraBridge)](https://github.com/bernard3378/AqaraBridge/stargazers) [![issues](https://img.shields.io/github/issues/bernard3378/AqaraBridge)](https://github.com/bernard3378/AqaraBridge/issues) [![hacs](https://img.shields.io/badge/HACS-Default-orange.svg)](https://hacs.xyz)

## One-Click Add to HACS
[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=bernard3378&repository=AqaraBridge&category=integration)

## Developer Account Required

Apply for an Aqara IoT Developer Account: [Aqara IoT Cloud](https://developer.aqara.com/register).

* Note: If you encounter an error during installation saying this integration does not support configuration via the UI, it is highly likely that the rocketmq library is missing. The current version only automatically integrates x86 and arm64 architectures.
* [V2.1.1] has added support for more architectures. If similar issues persist, please copy the log messages and submit an Issue.
* Currently, configuring via the HACS store is supported. Custom repository URL: bernard3378/AqaraBridge

Important Tips:
* You need to apply for your own Aqara developer account.
* Application Flow 1: [Register Account](https://developer.aqara.com/register). After approval, choose individual certification, and input your name and ID number to complete developer certification.
* Application Flow 2: Once approved, a DEMO application will be available. Go to Project Management --> Details --> Message Push --> Edit --> Select China Service (or the corresponding region), MQ Message Push, default message key (there should be only one), Full Subscription --> Save.
* Application Flow 3: Go back to Overview, expand Appid & Secret, find the service region (e.g., China Service), record the appId, appkey (click the eye icon to view), and keyid. Then input these three parameters into the corresponding fields in the integration setup.
* Message checking: If you need to confirm messages, change the log level of this integration to info to check the message logs.

## Version History
Current version V2.1.5 is a routine update, which is currently the most stable version.

V2.1.5
* Translated the entire codebase (including comments, docstrings, mapping constants, and entity names) from Chinese to English.
* Deleted the legacy `zh-Hans.json` translation file to enforce a 100% English-only integration.

V2.1.4
* Fixed the issue where token refresh was not awaited and signature arguments were missing during startup.
* Fixed climate entity (VRF and TCPECN02) caching and default attribute initialization to avoid AttributeError and KeyError.
* Optimized VRF and FP2 startup queries by using a single batch request instead of 30 sequential synchronous HTTP requests, preventing startup delays and 429 rate limit errors.

V2.1.3
* Fixed OptionsFlow crash and compatibility issues.
* Fixed typo in kelvin color temperature control and resolved feature failure.
* Fixed main thread lockup in HA caused by remote platform time.sleep.
* Removed deprecated air_quality platform code.
* Optimized config entry load flow to avoid race conditions.

V2.1.2
* Optimized startup wizard hints.
* Optimized device initialization flow.
* Optimized state management for presence sensor FP2.
* Optimized motion events for presence sensors FP1/FP1E.

- Added Devices:
- Hub / Gateway:
  - lumi.gateway.acn008 - Gateway M1S (2nd Gen)
  - lumi.gateway.acn012 - Hub M3

- Camera:
  - lumi.camera.gwpagl01 - Camera Hub G3 - Supports gestures and other events

- Switch / Plug:
  - lumi.switch.acn048 - Aqara Smart Wall Switch Z1 (Single Key)
  - lumi.switch.acn049 - Aqara Smart Wall Switch Z1 (Double Keys)
  - lumi.switch.acn054 - Aqara Smart Wall Switch Z1 (Triple Keys)
  - lumi.switch.acn055 - Aqara Smart Wall Switch Z1 (Quadruple Keys)
  - lumi.switch.acn056 - Aqara Smart Wall Switch Z1 Pro (Single Key)
  - lumi.switch.acn057 - Aqara Smart Wall Switch Z1 Pro (Double Keys)
  - lumi.switch.acn058 - Aqara Smart Wall Switch Z1 Pro (Triple Keys)
  - lumi.switch.acn059 - Aqara Smart Wall Switch Z1 Pro (Quadruple Keys)
  - lumi.switch.acn040 - Smart Wall Switch E1 (Neutral, Triple Keys)
  - lumi.switch.acn041 - Smart Wall Switch J1 (No Neutral, Single Key)
  - lumi.switch.acn042 - Smart Wall Switch J1 (No Neutral, Double Keys)
  - lumi.switch.acn043 - Smart Wall Switch J1 (No Neutral, Triple Keys)
  - lumi.switch.acn044 - Smart Wall Switch J1 (Neutral, Single Key)
  - lumi.switch.acn045 - Smart Wall Switch J1 (Neutral, Double Keys)
  - lumi.switch.acn046 - Smart Wall Switch J1 (Neutral, Triple Keys)
  - lumi.switch.acn062 - Smart Wall Switch Q1 (Single Key)
  - lumi.switch.acn063 - Smart Wall Switch Q1 (Double Keys)
  - lumi.switch.acn065 - Smart Wall Switch Q1 (Quadruple Keys)
  - lumi.switch.acn047 - Dual Relay Module T2
  - lumi.sensor_switch.v1 - Wireless Switch
  - lumi.sensor_switch.v2 - Wireless Switch
  - lumi.sensor_switch.aq2 - Wireless Switch

- Light Control: (Thanks to XaoflySho for the PR)
  - lumi.dimmer.acn003 - Smart LED Strip Driver T1
  - lumi.dimmer.acn004 - Smart LED Strip Driver T1 (120W)
  - lumi.dimmer.acn005 - Smart LED Strip Driver T1 (240W)

- Climate / Thermostat:
  - aqara.airrtc.acn02 - Thermostat Companion T1 (Indoor Unit)
  - lumi.airrtc.pcacn2 - Smart Thermostat S3
  - lumi.airrtc.pcacn2_thermostat - Smart Thermostat S3
  - lumi.airrtc.agl001 - Smart Valve Controller E1

- Cover / Curtain:
  - lumi.curtain.vagl02 - Smart Tubular Motor T1
  - lumi.curtain.acn002 - Roller Shade Companion E1

V2.1.1
* Fixed delay in curtain position synchronization.
* Updated functions deprecated in HA.
* Improved support for rocketmq on arm64 architecture.
* Optimized and resolved entity loading issues where unmanageable entities were created during initialization.
* Optimized cold startup wizard.
* Suppressed excessive warnings for partially supported devices.
* Changed button entities to event entities.

- Added Devices:
- Smart Clothes Dryer:
  - lumi.airer.acn001 - Smart Clothes Dryer H1
  - lumi.airer.acn02 - Aqara Smart Clothes Dryer Lite

V2.1.0
* Rewrote the AC/Climate controller implementation.
* Fixed issue where rocketmq startup blocked HA initialization.
* Fixed calls to deprecated/future deprecated constants in HA.
* Fixed color mapping errors in light entities.
* Fixed UI button issues for button entities.
* Fixed model matching error for Wireless Scene Switch (6-key).
* Optimized entity loading process.
* Optimized multi-channel device initialization.
* Optimized auto-naming rules for devices and entities.

- Added Devices:
- Hub / Gateway:
  - lumi.controller.a4acn1 - Magicpad S1

- Switch / Plug:
  - lumi.switch.n3acn3 - Smart Wall Switch D1 (Neutral, Triple Keys)
  - lumi.switch.l3acn3 - Smart Wall Switch D1 (No Neutral, Triple Keys)
  - lumi.ctrl_86plug.aq1 - Wall Socket (Zigbee version)
  - lumi.relay.c2acn01 - Dual Channel Controller

- Light Control:
  - lumi.light.cbacn1 - Aqara Smart Constant Current Driver T1-1
  - lumi.light.cwopcn01 - Ceiling Light MX960 (Color Temp adjustable)
  - lumi.light.acn007 - Track Grid Light H1 (6 heads)
  - lumi.light.acn008 - Track Grid Light H1 (12 heads)
  - lumi.light.acn009 - Track Flood Light H1 (30cm)
  - lumi.light.acn010 - Track Flood Light H1 (60cm)
  - lumi.light.acn011 - Track Pendant Light H1
  - lumi.light.acn012 - Track Folding Grid Light H1 (6 heads)
  - lumi.light.acn013 - Track Polarized Light H1 (22cm)
  - lumi.light.cwjwcn02 - Downlight (Color Temp adjustable)
  - lumi.light.acn004 - Aqara Dual Color Temp Driver T1 Pro
  - lumi.light.acn006 - Track Light H1 Pro
  - lumi.light.acn023 - Spotlight T2 (15 degrees)
  - lumi.light.acn024 - Spotlight T2 (24 degrees)
  - lumi.light.acn025 - Spotlight T2 (36 degrees)
  - lumi.light.acn026 - Downlight T2 (60 degrees)
  - lumi.light.acn128 - Spotlight/Downlight T3
  - lumi.light.acn014 - LED Bulb T1 (Color Temp adjustable)
  - lumi.light.acn003 - Aqara Ceiling Light L1-350
  - lumi.light.acn015 - Aqara skylight H1
  - lumi.light.acn032 - Smart Ceiling Light T1 (40W)
  - lumi.light.acn132 - LED Strip T1

- Cover / Curtain:
  - lumi.curtain.v1 - Smart Curtain Motor (Zigbee version)
  - lumi.curtain.acn007 - Aqara Smart Curtain Motor T1
  - lumi.curtain.hagl07 - Smart Curtain Motor C2
  - lumi.curtain.hagl08 - Aqara Smart Curtain Motor A1
  - lumi.curtain.hagl04 - Smart Curtain Motor B1
  - lumi.curtain.acn015 - Aqara Smart Curtain Motor T2
  - lumi.curtain.aq2 - Smart Tubular Motor
  - lumi.curtain.acn04 - Aqara Smart Curtain Motor C3
  - lumi.curtain.acn003 - Roller Shade Companion E1

- Climate / Thermostat:
  - lumi.aircondition.acn05 - Air Conditioner Companion P3
  - lumi.airrtc.vrfegl01 - VRF AC Controller
  - lumi.acpartner.aq1 - Air Conditioner Companion
  - lumi.acpartner.v3 - Air Conditioner Companion (Enhanced version)
  - lumi.ctrl_hvac.es1 - HVAC Thermostat
  - lumi.airrtc.tcpco2ecn01 - HVAC Thermostat (CO2)
  - lumi.acpartner.es1 - Air Conditioner Companion
  - lumi.airrtc.tcpecn01 - HVAC Thermostat
  - lumi.airrtc.tcpecn02 - HVAC Thermostat S2

- Sensors:
  - lumi.motion.ac02 - Motion Sensor P1
  - lumi.motion.agl02 - Motion Sensor T1
  - lumi.motion.acn001 - Motion Sensor E1
  - lumi.motion.agl001 - Presence Sensor FP2
  - lumi.sensor_occupy.agl1 - Presence Sensor FP1E
  - lumi.sensor_natgas.v1 - Natural Gas Alarm
  - lumi.sensor_gas.acn02 - Aqara Gas Alarm
  - lumi.airmonitor.acn01 - TVOC Air Quality Monitor
  - lumi.sen_ill.agl01 - Illuminance Sensor T1

V2.0.3
* Fixed developer configuration issues, allowing use of custom developer credentials.

V2.0.2
* Fixed issue with saving configuration incorrectly; added startup dependency requiring homekit setup to load first.
* Fixed option flow logic so that users can refresh expired tokens via phone number verification; resolved error warnings.
* Restructured Hass icons to correctly display integration and device manufacturer icons in the UI.
* Fixed general bugs.

V2.0.1
* Merged changes into master; dev branch is deprecated and will not be maintained.
* Consolidated multiple gateways to the account level, and permitted custom developer credentials (such as AppID, app_key, and key_id).
* Fixed state retrieval bugs and history state mappings.
* Special thanks to [Yinlang](https://bbs.hassbian.com/?62352) for adding wireless knob H1, H1 12-head magnetic track lights, wireless switch (enhanced version), power monitoring for wall switches (Neutral), and power monitoring for LED drivers.

V1.0.1
* Fixed issues across most components, and transitioned wireless switch events from polling to subscription to improve state updates.
* Added room/position retrieval.
* Added support for retrieving individual wireless switch button names.
* Added arm64 dynamic libraries for rocketmq (supporting x86 and arm64).
* Refreshed trigger_time / last_update_time for historical state data.
* Introduced button entity domain, splitting wireless switches from sensor entities.
* Configured common Aqara gateways, wireless switches, single/dual-wire switches, temperature/humidity sensors, smart plugs, and motion sensors.
* Added diagnostic error logging during initial config flow.

V1.0.0
* Initial release.

Note: This integration only supports devices I own or similar models. If you have unsupported devices and know Python, feel free to submit changes at:
[custom_components/aqara_bridge/core/aiot_mapping.py](https://github.com/meishild/AqaraBridge/blob/master/custom_components/aqara_bridge/core/aiot_mapping.py)

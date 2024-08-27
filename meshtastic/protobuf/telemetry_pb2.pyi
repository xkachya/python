"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _TelemetrySensorType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _TelemetrySensorTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_TelemetrySensorType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    SENSOR_UNSET: _TelemetrySensorType.ValueType  # 0
    """
    No external telemetry sensor explicitly set
    """
    BME280: _TelemetrySensorType.ValueType  # 1
    """
    High accuracy temperature, pressure, humidity
    """
    BME680: _TelemetrySensorType.ValueType  # 2
    """
    High accuracy temperature, pressure, humidity, and air resistance
    """
    MCP9808: _TelemetrySensorType.ValueType  # 3
    """
    Very high accuracy temperature
    """
    INA260: _TelemetrySensorType.ValueType  # 4
    """
    Moderate accuracy current and voltage
    """
    INA219: _TelemetrySensorType.ValueType  # 5
    """
    Moderate accuracy current and voltage
    """
    BMP280: _TelemetrySensorType.ValueType  # 6
    """
    High accuracy temperature and pressure
    """
    SHTC3: _TelemetrySensorType.ValueType  # 7
    """
    High accuracy temperature and humidity
    """
    LPS22: _TelemetrySensorType.ValueType  # 8
    """
    High accuracy pressure
    """
    QMC6310: _TelemetrySensorType.ValueType  # 9
    """
    3-Axis magnetic sensor
    """
    QMI8658: _TelemetrySensorType.ValueType  # 10
    """
    6-Axis inertial measurement sensor
    """
    QMC5883L: _TelemetrySensorType.ValueType  # 11
    """
    3-Axis magnetic sensor
    """
    SHT31: _TelemetrySensorType.ValueType  # 12
    """
    High accuracy temperature and humidity
    """
    PMSA003I: _TelemetrySensorType.ValueType  # 13
    """
    PM2.5 air quality sensor
    """
    INA3221: _TelemetrySensorType.ValueType  # 14
    """
    INA3221 3 Channel Voltage / Current Sensor
    """
    BMP085: _TelemetrySensorType.ValueType  # 15
    """
    BMP085/BMP180 High accuracy temperature and pressure (older Version of BMP280)
    """
    RCWL9620: _TelemetrySensorType.ValueType  # 16
    """
    RCWL-9620 Doppler Radar Distance Sensor, used for water level detection
    """
    SHT4X: _TelemetrySensorType.ValueType  # 17
    """
    Sensirion High accuracy temperature and humidity
    """
    VEML7700: _TelemetrySensorType.ValueType  # 18
    """
    VEML7700 high accuracy ambient light(Lux) digital 16-bit resolution sensor.
    """
    MLX90632: _TelemetrySensorType.ValueType  # 19
    """
    MLX90632 non-contact IR temperature sensor.
    """
    OPT3001: _TelemetrySensorType.ValueType  # 20
    """
    TI OPT3001 Ambient Light Sensor
    """
    LTR390UV: _TelemetrySensorType.ValueType  # 21
    """
    Lite On LTR-390UV-01 UV Light Sensor
    """
    TSL25911FN: _TelemetrySensorType.ValueType  # 22
    """
    AMS TSL25911FN RGB Light Sensor
    """
    AHT10: _TelemetrySensorType.ValueType  # 23
    """
    AHT10 Integrated temperature and humidity sensor
    """
    DFROBOT_LARK: _TelemetrySensorType.ValueType  # 24
    """
    DFRobot Lark Weather station (temperature, humidity, pressure, wind speed and direction)
    """
    NAU7802: _TelemetrySensorType.ValueType  # 25
    """
    NAU7802 Scale Chip or compatible
    """

class TelemetrySensorType(_TelemetrySensorType, metaclass=_TelemetrySensorTypeEnumTypeWrapper):
    """
    Supported I2C Sensors for telemetry in Meshtastic
    """

SENSOR_UNSET: TelemetrySensorType.ValueType  # 0
"""
No external telemetry sensor explicitly set
"""
BME280: TelemetrySensorType.ValueType  # 1
"""
High accuracy temperature, pressure, humidity
"""
BME680: TelemetrySensorType.ValueType  # 2
"""
High accuracy temperature, pressure, humidity, and air resistance
"""
MCP9808: TelemetrySensorType.ValueType  # 3
"""
Very high accuracy temperature
"""
INA260: TelemetrySensorType.ValueType  # 4
"""
Moderate accuracy current and voltage
"""
INA219: TelemetrySensorType.ValueType  # 5
"""
Moderate accuracy current and voltage
"""
BMP280: TelemetrySensorType.ValueType  # 6
"""
High accuracy temperature and pressure
"""
SHTC3: TelemetrySensorType.ValueType  # 7
"""
High accuracy temperature and humidity
"""
LPS22: TelemetrySensorType.ValueType  # 8
"""
High accuracy pressure
"""
QMC6310: TelemetrySensorType.ValueType  # 9
"""
3-Axis magnetic sensor
"""
QMI8658: TelemetrySensorType.ValueType  # 10
"""
6-Axis inertial measurement sensor
"""
QMC5883L: TelemetrySensorType.ValueType  # 11
"""
3-Axis magnetic sensor
"""
SHT31: TelemetrySensorType.ValueType  # 12
"""
High accuracy temperature and humidity
"""
PMSA003I: TelemetrySensorType.ValueType  # 13
"""
PM2.5 air quality sensor
"""
INA3221: TelemetrySensorType.ValueType  # 14
"""
INA3221 3 Channel Voltage / Current Sensor
"""
BMP085: TelemetrySensorType.ValueType  # 15
"""
BMP085/BMP180 High accuracy temperature and pressure (older Version of BMP280)
"""
RCWL9620: TelemetrySensorType.ValueType  # 16
"""
RCWL-9620 Doppler Radar Distance Sensor, used for water level detection
"""
SHT4X: TelemetrySensorType.ValueType  # 17
"""
Sensirion High accuracy temperature and humidity
"""
VEML7700: TelemetrySensorType.ValueType  # 18
"""
VEML7700 high accuracy ambient light(Lux) digital 16-bit resolution sensor.
"""
MLX90632: TelemetrySensorType.ValueType  # 19
"""
MLX90632 non-contact IR temperature sensor.
"""
OPT3001: TelemetrySensorType.ValueType  # 20
"""
TI OPT3001 Ambient Light Sensor
"""
LTR390UV: TelemetrySensorType.ValueType  # 21
"""
Lite On LTR-390UV-01 UV Light Sensor
"""
TSL25911FN: TelemetrySensorType.ValueType  # 22
"""
AMS TSL25911FN RGB Light Sensor
"""
AHT10: TelemetrySensorType.ValueType  # 23
"""
AHT10 Integrated temperature and humidity sensor
"""
DFROBOT_LARK: TelemetrySensorType.ValueType  # 24
"""
DFRobot Lark Weather station (temperature, humidity, pressure, wind speed and direction)
"""
NAU7802: TelemetrySensorType.ValueType  # 25
"""
NAU7802 Scale Chip or compatible
"""
global___TelemetrySensorType = TelemetrySensorType

@typing.final
class DeviceMetrics(google.protobuf.message.Message):
    """
    Key native device metrics such as battery level
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BATTERY_LEVEL_FIELD_NUMBER: builtins.int
    VOLTAGE_FIELD_NUMBER: builtins.int
    CHANNEL_UTILIZATION_FIELD_NUMBER: builtins.int
    AIR_UTIL_TX_FIELD_NUMBER: builtins.int
    UPTIME_SECONDS_FIELD_NUMBER: builtins.int
    battery_level: builtins.int
    """
    0-100 (>100 means powered)
    """
    voltage: builtins.float
    """
    Voltage measured
    """
    channel_utilization: builtins.float
    """
    Utilization for the current channel, including well formed TX, RX and malformed RX (aka noise).
    """
    air_util_tx: builtins.float
    """
    Percent of airtime for transmission used within the last hour.
    """
    uptime_seconds: builtins.int
    """
    How long the device has been running since the last reboot (in seconds)
    """
    def __init__(
        self,
        *,
        battery_level: builtins.int = ...,
        voltage: builtins.float = ...,
        channel_utilization: builtins.float = ...,
        air_util_tx: builtins.float = ...,
        uptime_seconds: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["air_util_tx", b"air_util_tx", "battery_level", b"battery_level", "channel_utilization", b"channel_utilization", "uptime_seconds", b"uptime_seconds", "voltage", b"voltage"]) -> None: ...

global___DeviceMetrics = DeviceMetrics

@typing.final
class EnvironmentMetrics(google.protobuf.message.Message):
    """
    Weather station or other environmental metrics
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TEMPERATURE_FIELD_NUMBER: builtins.int
    RELATIVE_HUMIDITY_FIELD_NUMBER: builtins.int
    BAROMETRIC_PRESSURE_FIELD_NUMBER: builtins.int
    GAS_RESISTANCE_FIELD_NUMBER: builtins.int
    VOLTAGE_FIELD_NUMBER: builtins.int
    CURRENT_FIELD_NUMBER: builtins.int
    IAQ_FIELD_NUMBER: builtins.int
    DISTANCE_FIELD_NUMBER: builtins.int
    LUX_FIELD_NUMBER: builtins.int
    WHITE_LUX_FIELD_NUMBER: builtins.int
    IR_LUX_FIELD_NUMBER: builtins.int
    UV_LUX_FIELD_NUMBER: builtins.int
    WIND_DIRECTION_FIELD_NUMBER: builtins.int
    WIND_SPEED_FIELD_NUMBER: builtins.int
    WEIGHT_FIELD_NUMBER: builtins.int
    WIND_GUST_FIELD_NUMBER: builtins.int
    WIND_LULL_FIELD_NUMBER: builtins.int
    temperature: builtins.float
    """
    Temperature measured
    """
    relative_humidity: builtins.float
    """
    Relative humidity percent measured
    """
    barometric_pressure: builtins.float
    """
    Barometric pressure in hPA measured
    """
    gas_resistance: builtins.float
    """
    Gas resistance in MOhm measured
    """
    voltage: builtins.float
    """
    Voltage measured (To be depreciated in favor of PowerMetrics in Meshtastic 3.x)
    """
    current: builtins.float
    """
    Current measured (To be depreciated in favor of PowerMetrics in Meshtastic 3.x)
    """
    iaq: builtins.int
    """
    relative scale IAQ value as measured by Bosch BME680 . value 0-500.
    Belongs to Air Quality but is not particle but VOC measurement. Other VOC values can also be put in here.
    """
    distance: builtins.float
    """
    RCWL9620 Doppler Radar Distance Sensor, used for water level detection. Float value in mm.
    """
    lux: builtins.float
    """
    VEML7700 high accuracy ambient light(Lux) digital 16-bit resolution sensor.
    """
    white_lux: builtins.float
    """
    VEML7700 high accuracy white light(irradiance) not calibrated digital 16-bit resolution sensor.
    """
    ir_lux: builtins.float
    """
    Infrared lux
    """
    uv_lux: builtins.float
    """
    Ultraviolet lux
    """
    wind_direction: builtins.int
    """
    Wind direction in degrees
    0 degrees = North, 90 = East, etc...
    """
    wind_speed: builtins.float
    """
    Wind speed in m/s
    """
    weight: builtins.float
    """
    Weight in KG
    """
    wind_gust: builtins.float
    """
    Wind gust in m/s
    """
    wind_lull: builtins.float
    """
    Wind lull in m/s
    """
    def __init__(
        self,
        *,
        temperature: builtins.float = ...,
        relative_humidity: builtins.float = ...,
        barometric_pressure: builtins.float = ...,
        gas_resistance: builtins.float = ...,
        voltage: builtins.float = ...,
        current: builtins.float = ...,
        iaq: builtins.int = ...,
        distance: builtins.float = ...,
        lux: builtins.float = ...,
        white_lux: builtins.float = ...,
        ir_lux: builtins.float = ...,
        uv_lux: builtins.float = ...,
        wind_direction: builtins.int = ...,
        wind_speed: builtins.float = ...,
        weight: builtins.float = ...,
        wind_gust: builtins.float = ...,
        wind_lull: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["barometric_pressure", b"barometric_pressure", "current", b"current", "distance", b"distance", "gas_resistance", b"gas_resistance", "iaq", b"iaq", "ir_lux", b"ir_lux", "lux", b"lux", "relative_humidity", b"relative_humidity", "temperature", b"temperature", "uv_lux", b"uv_lux", "voltage", b"voltage", "weight", b"weight", "white_lux", b"white_lux", "wind_direction", b"wind_direction", "wind_gust", b"wind_gust", "wind_lull", b"wind_lull", "wind_speed", b"wind_speed"]) -> None: ...

global___EnvironmentMetrics = EnvironmentMetrics

@typing.final
class PowerMetrics(google.protobuf.message.Message):
    """
    Power Metrics (voltage / current / etc)
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CH1_VOLTAGE_FIELD_NUMBER: builtins.int
    CH1_CURRENT_FIELD_NUMBER: builtins.int
    CH2_VOLTAGE_FIELD_NUMBER: builtins.int
    CH2_CURRENT_FIELD_NUMBER: builtins.int
    CH3_VOLTAGE_FIELD_NUMBER: builtins.int
    CH3_CURRENT_FIELD_NUMBER: builtins.int
    ch1_voltage: builtins.float
    """
    Voltage (Ch1)
    """
    ch1_current: builtins.float
    """
    Current (Ch1)
    """
    ch2_voltage: builtins.float
    """
    Voltage (Ch2)
    """
    ch2_current: builtins.float
    """
    Current (Ch2)
    """
    ch3_voltage: builtins.float
    """
    Voltage (Ch3)
    """
    ch3_current: builtins.float
    """
    Current (Ch3)
    """
    def __init__(
        self,
        *,
        ch1_voltage: builtins.float = ...,
        ch1_current: builtins.float = ...,
        ch2_voltage: builtins.float = ...,
        ch2_current: builtins.float = ...,
        ch3_voltage: builtins.float = ...,
        ch3_current: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["ch1_current", b"ch1_current", "ch1_voltage", b"ch1_voltage", "ch2_current", b"ch2_current", "ch2_voltage", b"ch2_voltage", "ch3_current", b"ch3_current", "ch3_voltage", b"ch3_voltage"]) -> None: ...

global___PowerMetrics = PowerMetrics

@typing.final
class AirQualityMetrics(google.protobuf.message.Message):
    """
    Air quality metrics
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PM10_STANDARD_FIELD_NUMBER: builtins.int
    PM25_STANDARD_FIELD_NUMBER: builtins.int
    PM100_STANDARD_FIELD_NUMBER: builtins.int
    PM10_ENVIRONMENTAL_FIELD_NUMBER: builtins.int
    PM25_ENVIRONMENTAL_FIELD_NUMBER: builtins.int
    PM100_ENVIRONMENTAL_FIELD_NUMBER: builtins.int
    PARTICLES_03UM_FIELD_NUMBER: builtins.int
    PARTICLES_05UM_FIELD_NUMBER: builtins.int
    PARTICLES_10UM_FIELD_NUMBER: builtins.int
    PARTICLES_25UM_FIELD_NUMBER: builtins.int
    PARTICLES_50UM_FIELD_NUMBER: builtins.int
    PARTICLES_100UM_FIELD_NUMBER: builtins.int
    pm10_standard: builtins.int
    """
    Concentration Units Standard PM1.0
    """
    pm25_standard: builtins.int
    """
    Concentration Units Standard PM2.5
    """
    pm100_standard: builtins.int
    """
    Concentration Units Standard PM10.0
    """
    pm10_environmental: builtins.int
    """
    Concentration Units Environmental PM1.0
    """
    pm25_environmental: builtins.int
    """
    Concentration Units Environmental PM2.5
    """
    pm100_environmental: builtins.int
    """
    Concentration Units Environmental PM10.0
    """
    particles_03um: builtins.int
    """
    0.3um Particle Count
    """
    particles_05um: builtins.int
    """
    0.5um Particle Count
    """
    particles_10um: builtins.int
    """
    1.0um Particle Count
    """
    particles_25um: builtins.int
    """
    2.5um Particle Count
    """
    particles_50um: builtins.int
    """
    5.0um Particle Count
    """
    particles_100um: builtins.int
    """
    10.0um Particle Count
    """
    def __init__(
        self,
        *,
        pm10_standard: builtins.int = ...,
        pm25_standard: builtins.int = ...,
        pm100_standard: builtins.int = ...,
        pm10_environmental: builtins.int = ...,
        pm25_environmental: builtins.int = ...,
        pm100_environmental: builtins.int = ...,
        particles_03um: builtins.int = ...,
        particles_05um: builtins.int = ...,
        particles_10um: builtins.int = ...,
        particles_25um: builtins.int = ...,
        particles_50um: builtins.int = ...,
        particles_100um: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["particles_03um", b"particles_03um", "particles_05um", b"particles_05um", "particles_100um", b"particles_100um", "particles_10um", b"particles_10um", "particles_25um", b"particles_25um", "particles_50um", b"particles_50um", "pm100_environmental", b"pm100_environmental", "pm100_standard", b"pm100_standard", "pm10_environmental", b"pm10_environmental", "pm10_standard", b"pm10_standard", "pm25_environmental", b"pm25_environmental", "pm25_standard", b"pm25_standard"]) -> None: ...

global___AirQualityMetrics = AirQualityMetrics

@typing.final
class Telemetry(google.protobuf.message.Message):
    """
    Types of Measurements the telemetry module is equipped to handle
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TIME_FIELD_NUMBER: builtins.int
    DEVICE_METRICS_FIELD_NUMBER: builtins.int
    ENVIRONMENT_METRICS_FIELD_NUMBER: builtins.int
    AIR_QUALITY_METRICS_FIELD_NUMBER: builtins.int
    POWER_METRICS_FIELD_NUMBER: builtins.int
    time: builtins.int
    """
    Seconds since 1970 - or 0 for unknown/unset
    """
    @property
    def device_metrics(self) -> global___DeviceMetrics:
        """
        Key native device metrics such as battery level
        """

    @property
    def environment_metrics(self) -> global___EnvironmentMetrics:
        """
        Weather station or other environmental metrics
        """

    @property
    def air_quality_metrics(self) -> global___AirQualityMetrics:
        """
        Air quality metrics
        """

    @property
    def power_metrics(self) -> global___PowerMetrics:
        """
        Power Metrics
        """

    def __init__(
        self,
        *,
        time: builtins.int = ...,
        device_metrics: global___DeviceMetrics | None = ...,
        environment_metrics: global___EnvironmentMetrics | None = ...,
        air_quality_metrics: global___AirQualityMetrics | None = ...,
        power_metrics: global___PowerMetrics | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["air_quality_metrics", b"air_quality_metrics", "device_metrics", b"device_metrics", "environment_metrics", b"environment_metrics", "power_metrics", b"power_metrics", "variant", b"variant"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["air_quality_metrics", b"air_quality_metrics", "device_metrics", b"device_metrics", "environment_metrics", b"environment_metrics", "power_metrics", b"power_metrics", "time", b"time", "variant", b"variant"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["variant", b"variant"]) -> typing.Literal["device_metrics", "environment_metrics", "air_quality_metrics", "power_metrics"] | None: ...

global___Telemetry = Telemetry

@typing.final
class Nau7802Config(google.protobuf.message.Message):
    """
    NAU7802 Telemetry configuration, for saving to flash
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ZEROOFFSET_FIELD_NUMBER: builtins.int
    CALIBRATIONFACTOR_FIELD_NUMBER: builtins.int
    zeroOffset: builtins.int
    """
    The offset setting for the NAU7802
    """
    calibrationFactor: builtins.float
    """
    The calibration factor for the NAU7802
    """
    def __init__(
        self,
        *,
        zeroOffset: builtins.int = ...,
        calibrationFactor: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["calibrationFactor", b"calibrationFactor", "zeroOffset", b"zeroOffset"]) -> None: ...

global___Nau7802Config = Nau7802Config

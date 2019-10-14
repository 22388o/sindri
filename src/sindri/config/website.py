"""
Configuration for the plots and tables on the Mjolnir website.
"""

# Standard library imports
import datetime

# Local imports
from sindri.utils.misc import WEBSITE_UPDATE_INTERVAL_S as UPDATE_INT
from sindri.website.templates import (
    GAUGE_PLOT_UPDATE_CODE,
    GAUGE_PLOT_UPDATE_CODE_VALUE,
    GAUGE_PLOT_UPDATE_CODE_COLOR,
    generate_step_string,
)


STATUS_UPDATE_INTERVAL_SECONDS = 10
STATUS_UPDATE_INTERVAL_FAST_SECONDS = 1


STATUS_DASHBOARD_PLOTS = {
    "weblatency": {
        "plot_type": None,
        "plot_data": {},
        "plot_metadata": {
            "plot_title": "Website Latency",
            "plot_description": "",
            },
        "plot_params": {
            "gauge_value": 0,
            "plot_mode": "gauge+number+delta",
            "delta_reference": UPDATE_INT,
            "decreasing_color": "green",
            "increasing_color": "red",
            "dtick": UPDATE_INT / 2,
            "range": [0, UPDATE_INT * 2],
            "tick0": 0,
            "steps": generate_step_string((
                ([0, UPDATE_INT], "green"),
                ([UPDATE_INT, UPDATE_INT + 60], "lime"),
                ([UPDATE_INT + 60, UPDATE_INT + 2 * 60], "yellow"),
                ([UPDATE_INT + 2 * 60, UPDATE_INT + 3 * 60], "orange"),
                ([UPDATE_INT + 3 * 60, 32 * 24 * 60 * 60], "red"),
                )),
            "threshold_thickness": 0.75,
            "threshold_value": 0,
            "number_color": "white",
            "number_suffix": " s",
            "plot_update_code": (
                "data['value'] = (new Date() "
                "- lastUpdate_status) / (1000);\n"
                "if (data['value'] > maxLatency_status) {\n"
                "    maxLatency_status = data['value'];\n"
                "    data['gauge.threshold.value'] = data['value'];\n"
                "};\n"
                + GAUGE_PLOT_UPDATE_CODE_COLOR
                ),
            },
        "fast_update": True,
        },
    "datalatency": {
        "plot_type": "numeric",
        "plot_data": {
            "data_functions": (lambda base_data, data_args: base_data[-1], ),
            "variable": (lambda full_data:
                         (datetime.datetime.now() - full_data.index)
                         .total_seconds())
            },
        "plot_metadata": {
            "plot_title": "Data Latency",
            "plot_description": "",
            },
        "plot_params": {
            "gauge_value": "NaN",
            "plot_mode": "gauge+number+delta",
            "delta_reference": 60,
            "decreasing_color": "green",
            "increasing_color": "red",
            "dtick": 60,
            "range": [0, 300],
            "tick0": 0,
            "steps": generate_step_string((
                ([0, 60], "green"),
                ([60, 120], "yellow"),
                ([120, 240], "orange"),
                ([240, 32 * 24 * 60 * 60], "red"),
                )),
            "threshold_thickness": 0.75,
            "threshold_value": 60,
            "number_color": "white",
            "number_suffix": " s",
            "plot_update_code": (
                "\n".join((
                    *GAUGE_PLOT_UPDATE_CODE_VALUE
                    .splitlines()[0:2],
                    GAUGE_PLOT_UPDATE_CODE_COLOR
                    ))),
            },
        "fast_update": False,
        },
    "sensoruptime": {
        "plot_type": "numeric",
        "plot_data": {
            "delta_period": "1H",
            "threshold_period": "24H",
            "threshold_type": "max",
            "variable": "sensor_uptime",
            },
        "plot_metadata": {
            "plot_title": "Sensor Uptime",
            "plot_description": "",
            },
        "plot_params": {
            "gauge_value": "NaN",
            "plot_mode": "gauge+number+delta",
            "delta_reference": "NaN",
            "decreasing_color": "red",
            "increasing_color": "green",
            "dtick": 120,
            "range": [0, 30 * 24],
            "tick0": 0,
            "steps": generate_step_string((
                ([0.0, 1.0], "red"),
                ([1.0, 6.0], "orange"),
                ([6.0, 24.], "yellow"),
                ([24., 48.], "lime"),
                ([48., 999], "green"),
                )),
            "threshold_thickness": 0.75,
            "threshold_value": 0,
            "number_color": "white",
            "number_suffix": " h",
            "plot_update_code": GAUGE_PLOT_UPDATE_CODE,
            },
        "fast_update": False,
        },
    "battvoltage": {
        "plot_type": "numeric",
        "plot_data": {
            "delta_period": "1H",
            "threshold_period": "24H",
            "threshold_type": "min",
            "variable": "adc_vb_f",
            },
        "plot_metadata": {
            "plot_title": "Battery Voltage",
            "plot_description": "",
            },
        "plot_params": {
            "gauge_value": "NaN",
            "plot_mode": "gauge+number+delta",
            "delta_reference": "NaN",
            "decreasing_color": "red",
            "increasing_color": "green",
            "dtick": 1,
            "range": [10, 15],
            "tick0": 10,
            "steps": generate_step_string((
                ([0.00, 10.4], "red"),
                ([10.4, 11.0], "orange"),
                ([11.0, 11.5], "yellow"),
                ([11.5, 12.0], "lime"),
                ([12.0, 14.0], "green"),
                ([14.0, 14.3], "lime"),
                ([14.3, 14.6], "yellow"),
                ([14.6, 15.0], "orange"),
                ([15.0, 99.9], "red"),
                )),
            "threshold_thickness": 0.75,
            "threshold_value": 0,
            "number_color": "white",
            "number_suffix": " V",
            "plot_update_code": GAUGE_PLOT_UPDATE_CODE,
            },
        "fast_update": False,
        },
    "arrayvoltage": {
        "plot_type": "numeric",
        "plot_data": {
            "delta_period": "1H",
            "threshold_period": "24H",
            "threshold_type": "max",
            "variable": "adc_va_f",
            },
        "plot_metadata": {
            "plot_title": "Array Voltage",
            "plot_description": "",
            },
        "plot_params": {
            "gauge_value": "NaN",
            "plot_mode": "gauge+number+delta",
            "delta_reference": "NaN",
            "decreasing_color": "red",
            "increasing_color": "green",
            "dtick": 12,
            "range": [0, 60],
            "tick0": 0,
            "steps": generate_step_string((
                ([0.00, 4.00], "red"),
                ([4.00, 12.0], "orange"),
                ([12.0, 24.0], "yellow"),
                ([24.0, 32.0], "lime"),
                ([32.0, 64.0], "green"),
                )),
            "threshold_thickness": 0.75,
            "threshold_value": 0,
            "number_color": "white",
            "number_suffix": " V",
            "plot_update_code": GAUGE_PLOT_UPDATE_CODE,
            },
        "fast_update": False,
        },
    "chargecurrent": {
        "plot_type": "numeric",
        "plot_data": {
            "delta_period": "1H",
            "threshold_period": "24H",
            "threshold_type": "max",
            "variable": "adc_ic_f",
            },
        "plot_metadata": {
            "plot_title": "Charging Current",
            "plot_description": "",
            },
        "plot_params": {
            "gauge_value": "NaN",
            "plot_mode": "gauge+number+delta",
            "delta_reference": "NaN",
            "decreasing_color": "red",
            "increasing_color": "green",
            "dtick": 2,
            "range": [0, 12],
            "tick0": 0,
            "steps": generate_step_string((
                ([0.0, 0.1], "red"),
                ([0.1, 0.5], "orange"),
                ([0.5, 1.0], "yellow"),
                ([1.0, 2.0], "lime"),
                ([2.0, 20.], "green"),
                )),
            "threshold_thickness": 0.75,
            "threshold_value": 0,
            "number_color": "white",
            "number_suffix": " A",
            "plot_update_code": GAUGE_PLOT_UPDATE_CODE,
            },
        "fast_update": False,
        },
    "chargestate": {
        "plot_type": "numeric",
        "plot_data": {
            "delta_period": "1H",
            "threshold_period": "24H",
            "threshold_type": "max",
            "variable": "charge_state",
            },
        "plot_metadata": {
            "plot_title": "Charge State",
            "plot_description": "",
            },
        "plot_params": {
            "gauge_value": "NaN",
            "plot_mode": "gauge+number+delta",
            "delta_reference": "NaN",
            "decreasing_color": "red",
            "increasing_color": "green",
            "dtick": 1,
            "range": [0, 8],
            "tick0": 0,
            "steps": generate_step_string((
                ([0.0, 0.5], "gray"),
                ([0.5, 1.5], "blue"),
                ([1.5, 2.5], "maroon"),
                ([2.5, 3.5], "orange"),
                ([3.5, 4.5], "red"),
                ([4.5, 5.5], "yellow"),
                ([5.5, 6.5], "lime"),
                ([6.5, 7.5], "green"),
                ([7.5, 8.5], "teal"),
                )),
            "threshold_thickness": 0.75,
            "threshold_value": 0,
            "number_color": "white",
            "number_suffix": "",
            "plot_update_code": GAUGE_PLOT_UPDATE_CODE,
            },
        "fast_update": False,
        },
    "loadpower": {
        "plot_type": "numeric",
        "plot_data": {
            "delta_period": "1H",
            "threshold_period": "24H",
            "threshold_type": "min",
            "variable": "power_load",
            },
        "plot_metadata": {
            "plot_title": "Load Power",
            "plot_description": "",
            },
        "plot_params": {
            "gauge_value": "NaN",
            "plot_mode": "gauge+number+delta",
            "delta_reference": "NaN",
            "decreasing_color": "blue",
            "increasing_color": "orange",
            "dtick": 5,
            "range": [0, 30],
            "tick0": 0,
            "steps": generate_step_string((
                ([0.00, 1.00], "red"),
                ([1.00, 8.00], "orange"),
                ([8.00, 12.0], "yellow"),
                ([12.0, 13.5], "lime"),
                ([13.5, 16.0], "green"),
                ([16.0, 18.0], "teal"),
                ([18.0, 19.0], "lime"),
                ([19.0, 20.0], "yellow"),
                ([20.0, 25.0], "orange"),
                ([25.0, 99.9], "red"),
                )),
            "threshold_thickness": 0.75,
            "threshold_value": 0,
            "number_color": "white",
            "number_suffix": " W",
            "plot_update_code": GAUGE_PLOT_UPDATE_CODE,
            },
        "fast_update": False,
        },
    "batterytemp": {
        "plot_type": "numeric",
        "plot_data": {
            "delta_period": "1H",
            "threshold_period": "24H",
            "threshold_type": "max",
            "variable": "t_batt",
            },
        "plot_metadata": {
            "plot_title": "Battery Temperature",
            "plot_description": "",
            },
        "plot_params": {
            "gauge_value": "NaN",
            "plot_mode": "gauge+number+delta",
            "delta_reference": "NaN",
            "decreasing_color": "blue",
            "increasing_color": "orange",
            "dtick": 20,
            "range": [-20, 80],
            "tick0": -20,
            "steps": generate_step_string((
                ([-20, -10], "white"),
                ([-10, 0.0], "blue"),
                ([0.0, 10.], "teal"),
                ([10., 50.], "green"),
                ([50., 60.], "yellow"),
                ([60., 70.], "orange"),
                ([70., 200], "red"),
                )),
            "threshold_thickness": 0.75,
            "threshold_value": 0,
            "number_color": "white",
            "number_suffix": "°C",
            "plot_update_code": GAUGE_PLOT_UPDATE_CODE,
            },
        "fast_update": False,
        },
    "triggerrate": {
        "plot_type": "numeric",
        "plot_data": {
            "delta_period": "1H",
            "threshold_period": "24H",
            "threshold_type": "max",
            "variable": "trigger_rate_5min",
            },
        "plot_metadata": {
            "plot_title": "Trigger Rate",
            "plot_description": "",
            },
        "plot_params": {
            "gauge_value": "NaN",
            "plot_mode": "gauge+number+delta",
            "delta_reference": "NaN",
            "decreasing_color": "blue",
            "increasing_color": "orange",
            "dtick": 10,
            "range": [0, 60],
            "tick0": 0,
            "steps": generate_step_string((
                ([0.0, 0.4], "gray"),
                ([0.4, 1.4], "blue"),
                ([1.4, 5.0], "teal"),
                ([5.0, 10.], "green"),
                ([10., 20.], "lime"),
                ([20., 30.], "yellow"),
                ([30., 40.], "orange"),
                ([40., 50.], "red"),
                ([50., 99.], "maroon"),
                )),
            "threshold_thickness": 0.75,
            "threshold_value": 0,
            "number_color": "white",
            "number_suffix": "/min",
            "plot_update_code": GAUGE_PLOT_UPDATE_CODE,
            },
        "fast_update": False,
        },
    "triggersremaining": {
        "plot_type": "numeric",
        "plot_data": {
            "delta_period": "1H",
            "threshold_period": "24H",
            "threshold_type": "max",
            "variable": "triggers_remaining",
            },
        "plot_metadata": {
            "plot_title": "Triggers Remaining",
            "plot_description": "",
            },
        "plot_params": {
            "gauge_value": "NaN",
            "plot_mode": "gauge+number+delta",
            "delta_reference": "NaN",
            "decreasing_color": "red",
            "increasing_color": "green",
            "dtick": 3600,
            "range": [0, 21600],
            "tick0": 0,
            "steps": generate_step_string((
                ([0.000, 60.00], "red"),
                ([60.00, 1800.], "orange"),
                ([1800., 3600.], "yellow"),
                ([3600., 7200.], "lime"),
                ([7200., 99999], "green"),
                )),
            "threshold_thickness": 0.75,
            "threshold_value": 0,
            "number_color": "white",
            "number_suffix": "",
            "plot_update_code": GAUGE_PLOT_UPDATE_CODE,
            },
        "fast_update": False,
        },
    "crcerrors": {
        "plot_type": "custom",
        "plot_data": {
            "data_functions": (
                lambda full_data, data_args:
                full_data.loc[:, "crc_errors_daily"].iloc[-1],
                lambda full_data, data_args:
                full_data.loc[:, "crc_errors_hourly"].iloc[-1],
                lambda full_data, data_args:
                full_data["crc_errors"].last("24H").max(),
                ),
            },
        "plot_metadata": {
            "plot_title": "CRC Errors",
            "plot_description": "",
            },
        "plot_params": {
            "gauge_value": "NaN",
            "plot_mode": "gauge+number+delta",
            "delta_reference": "NaN",
            "decreasing_color": "green",
            "increasing_color": "red",
            "dtick": 20,
            "range": [0, 100],
            "tick0": 0,
            "steps": generate_step_string((
                ([0.00, 0.90], "green"),
                ([0.90, 5.00], "lime"),
                ([5.00, 12.5], "yellow"),
                ([12.5, 25.0], "orange"),
                ([25.0, 50.0], "red"),
                ([50.0, 9999], "maroon"),
                )),
            "threshold_thickness": 0.75,
            "threshold_value": 0,
            "number_color": "white",
            "number_suffix": "",
            "plot_update_code": GAUGE_PLOT_UPDATE_CODE,
            },
        "fast_update": False,
        },
    }


STATUS_DASHBOARD_METADATA = {
    "section_id": "status",
    "section_title": "Status Dashboard",
    "section_description": (
        "Real-time status of this HAMMA sensor and the Mjolnir system."),
    "section_nav_label": "Status",
    }


STATUS_DASHBOARD_ARGS = {
    "dashboard_plots": STATUS_DASHBOARD_PLOTS,
    "update_interval_seconds": STATUS_UPDATE_INTERVAL_SECONDS,
    "update_interval_fast_seconds": (
        STATUS_UPDATE_INTERVAL_FAST_SECONDS),
    }


LOG_METADATA = {
    "section_id": "log",
    "section_title": "Client Log",
    "section_description": (
        "Latest log entries from this sensor's Brokkr client."),
    "section_nav_label": "Log",
    "button_content": "View Full Log",
    "button_type": "text",
    "button_position": "bottom",
    "button_newtab": "false",
    }


LOG_DATA_ARGS = {
    "input_path": "~/brokkr.log",
    "output_path": "brokkr_log_latest.txt",
    "output_path_full": "brokkr_log_full.txt",
    "n_lines": 30,
    }


LOG_REPLACE_ITEMS = [
    ["CRITICAL", "<span class='log-highlight critical'>CRITICAL</span>"],
    ["ERROR", "<span class='log-highlight error'>ERROR</span>"],
    ["WARNING", "<span class='log-highlight warning'>WARNING</span>"],
    ["INFO", "<span class='log-highlight info'>INFO</span>"],
    ["DEBUG", "<span class='log-highlight debug'>DEBUG</span>"],
    ["\\|", "<span class='pipe-colored log-pipe'>|</span>"],
    ]


LOG_ARGS = {
    "data_args": LOG_DATA_ARGS,
    "replace_items": LOG_REPLACE_ITEMS,
    "update_interval_seconds": STATUS_UPDATE_INTERVAL_SECONDS,
    }


MAINPAGE_BLOCKS = (
    ("dashboard", STATUS_DASHBOARD_METADATA, STATUS_DASHBOARD_ARGS),
    ("text", LOG_METADATA, LOG_ARGS),
    )

from cat.mad_hatter.decorators import tool,hook,plugin
from datetime import date
from .openWeather import WeatherAPI





@tool()
def get_weather(tool_input,cat):
    """Replies to "weather today","what the weather will be like on Tuesday","What will the weather be like this weekend?" and similar questions. Input is always None..,
        the input is the day"""
    settings = cat.mad_hatter.plugins["wonderland_weather"].load_settings()
    
    weather_api = WeatherAPI(settings["OpenWeather_api"], settings["city"], settings["Temperature_unit"])
    weather_data = weather_api.weather()
    
    if(weather_data):
        return weather_data



@hook
def agent_prompt_prefix(prefix,cat):
    settings = cat.mad_hatter.plugins["wonderland_weather"].load_settings()
    data_odierna = date.today()
    data_format = data_odierna.strftime("%A %Y-%m-%d")
    return f"""Today is: {data_format} and we live in {settings["city"]}"""


@hook
def agent_fast_reply(fast_reply, cat):

    settings = cat.mad_hatter.plugins["wonderland_weather"].load_settings()
    
    if "OpenWeather_api" not in settings:
        fast_reply["output"]="you need to set the openWeather api key in the plugin settings to continue asking me questions"
        return fast_reply
    
    return fast_reply
    

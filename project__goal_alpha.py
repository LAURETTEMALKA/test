{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNiyxXpzoADtv8O3uE2PpMP",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/LAURETTEMALKA/test/blob/main/project__goal_alpha.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## **PROJECT 1:**\n",
        " *WHEATHER CHECKER APPLICATION*"
      ],
      "metadata": {
        "id": "qCsUFCMmhZL9"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install streamlit\n",
        "!pip install requests\n",
        "import streamlit as st"
      ],
      "metadata": {
        "id": "70GgDCEScnIG"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "st.title('Whath\\'s the Wheather ')\n",
        "\n",
        "import pytz\n",
        "timezone_option= pytz.all_timezones\n",
        "\n",
        "while user_timezone not in timezone_option:\n",
        "    user_timezone =st.text_input(\"Enter your location: \")\n",
        "\n",
        "if user_timezone:\n",
        "    st.write(f\"You are in, {user_timezone}!\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 408
        },
        "id": "guWSWGMXiHzD",
        "outputId": "6003fcd7-5704-4b49-9750-451b29285fd9"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "error",
          "ename": "KeyboardInterrupt",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-5-27bb82548cd2>\u001b[0m in \u001b[0;36m<cell line: 6>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      6\u001b[0m \u001b[0;32mwhile\u001b[0m \u001b[0muser_timezone\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mtimezone_option\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 7\u001b[0;31m     \u001b[0muser_timezone\u001b[0m \u001b[0;34m=\u001b[0m\u001b[0mst\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtext_input\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Enter your location: \"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      8\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      9\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0muser_timezone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/streamlit/runtime/metrics_util.py\u001b[0m in \u001b[0;36mwrapped_func\u001b[0;34m(*args, **kwargs)\u001b[0m\n\u001b[1;32m    394\u001b[0m                 \u001b[0m_LOGGER\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdebug\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Failed to collect command telemetry\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mexc_info\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mex\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    395\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 396\u001b[0;31m             \u001b[0mresult\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mnon_optional_func\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    397\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mRerunException\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mex\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    398\u001b[0m             \u001b[0;31m# Duplicated from below, because static analysis tools get confused\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/streamlit/elements/widgets/text_widgets.py\u001b[0m in \u001b[0;36mtext_input\u001b[0;34m(self, label, value, max_chars, key, type, help, autocomplete, on_change, args, kwargs, placeholder, disabled, label_visibility)\u001b[0m\n\u001b[1;32m    219\u001b[0m         \"\"\"\n\u001b[1;32m    220\u001b[0m         \u001b[0mctx\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mget_script_run_ctx\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 221\u001b[0;31m         return self._text_input(\n\u001b[0m\u001b[1;32m    222\u001b[0m             \u001b[0mlabel\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mlabel\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    223\u001b[0m             \u001b[0mvalue\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mvalue\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/streamlit/elements/widgets/text_widgets.py\u001b[0m in \u001b[0;36m_text_input\u001b[0;34m(self, label, value, max_chars, key, type, help, autocomplete, on_change, args, kwargs, placeholder, disabled, label_visibility, ctx)\u001b[0m\n\u001b[1;32m    333\u001b[0m             \u001b[0mtext_input_proto\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mset_value\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mTrue\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    334\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 335\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdg\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_enqueue\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"text_input\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtext_input_proto\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    336\u001b[0m         \u001b[0;32mreturn\u001b[0m \u001b[0mwidget_state\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mvalue\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    337\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m: "
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import datetime as dt"
      ],
      "metadata": {
        "id": "YmpLeIlRcZQY"
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def display_date_time(user_timezone, location_timezone=None):\n",
        "    # Fetch current date and time in user's timezone\n",
        "    user_time = datetime.now(pytz.timezone(user_timezone))\n",
        "    formatted_user_time = user_time.strftime(\"%A, %B %d, %Y, %I:%M %p\")\n",
        "    st.write(f\"Your current date and time: {formatted_user_time}\")\n",
        "\n",
        "    API = 'e1313973fe262c3c18b4500d98fe65eb'\n",
        "    url=f\"https://api.openweathermap.org/data/2.5/weather?appid={API}&q={user_timezone}\"\n",
        "    weatherzone= rq.get(url)\n",
        "    response_weatherzone=weatherzone.json()\n",
        "    print(response_weatherzone)\n",
        "\n",
        "    humidity=response_weatherzone['main']['humidity']\n",
        "    pressure=response_weatherzone['main']['pressure']\n",
        "    wind=response_weatherzone['wind']['speed']\n",
        "    description=response_weatherzone['weather'][0]['description']\n",
        "    temp=response_weatherzone['main']['temp']\n",
        "\n",
        "    st.write(f'Temperature:', {temp},'°C')\n",
        "    st.write(f'Wind:', {wind})\n",
        "    st.write(f'Pressure:', {pressure})\n",
        "    st.write(f'Humidity:', {humidity})\n",
        "    st.write(f'Description:', {description})\n",
        "\n",
        "    # Optional: Convert and display the date and time for the specified location\n",
        "    if location_timezone:\n",
        "        location_time = user_time.astimezone(pytz.timezone(location_timezone))\n",
        "        formatted_location_time = location_time.strftime(\"%A, %B %d, %Y, %I:%M %p\")\n",
        "        st.write(f\"Date and time in {location_timezone}: {formatted_location_time}\")"
      ],
      "metadata": {
        "id": "S801ju3KoLl9"
      },
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#current_local_date_and_time = dt.datetime.now(pytz.timezone(city_name))\n",
        "#current_local_date_and_time"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QNZzs7b7ltwM",
        "outputId": "1d8ef826-56f9-430d-b008-f6e892ec957f"
      },
      "execution_count": 42,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "datetime.datetime(2023, 11, 28, 13, 5, 53, 919535, tzinfo=<DstTzInfo 'Israel' IST+2:00:00 STD>)"
            ]
          },
          "metadata": {},
          "execution_count": 42
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#format_a = current_local_date_and_time.strftime(\"%d.%m.%Y\")\n",
        "#print(format_c)\n",
        "#format_D = current_local_date_and_time.strftime(\"%H:%M:%S:%f\")\n",
        "#print(format_D)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QKz-KVbuO-VI",
        "outputId": "118c964b-cfa6-41d2-d3d6-b4f0f437e8ce"
      },
      "execution_count": 43,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "28.11.2023\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Today we are the\", user_time.strftime(\"%d.%m.%Y\"),\"and it's\",user_time.strftime(\"%H:%M:%S:%f\")\n",
        " )"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wZPw8FanRnIp",
        "outputId": "0b0ed71e-37cc-4376-cdd8-85f04ca99144"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Today we are the 27.11.2023 and it's 19:21:55:883671\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#print(\"Today we are the\", current_local_date_and_time.strftime(\"%d %b %Y\"),\"and it's\",current_local_date_and_time.strftime(\"%H\"),\"hours\", current_local_date_and_time.strftime(\"%M\"),\"minutes and\", current_local_date_and_time.strftime(\"%S\"),\"secondes.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3GANxKKzSIRz",
        "outputId": "60f3b0a3-32da-48d9-b519-4808783117f2"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Today we are the 27 Nov 2023 and it's 19 hours 21 minutes and 55 secondes.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#city_name = input(\"Enter City:\")\n",
        "#API = 'e1313973fe262c3c18b4500d98fe65eb'\n",
        "#url=f\"https://api.openweathermap.org/data/2.5/weather?appid={API}&q={city_name}\"\n",
        "#weatherzone= rq.get(url)\n",
        "#response_weatherzone=weatherzone.json()\n",
        "#print(response_weatherzone)\n",
        "\n",
        "#humidity=response_weatherzone['main']['humidity']\n",
        "#pressure=response_weatherzone['main']['pressure']\n",
        "#wind=response_weatherzone['wind']['speed']\n",
        "#description=response_weatherzone['weather'][0]['description']\n",
        "#temp=response_weatherzone['main']['temp']\n",
        "\n",
        "#print('Temperature:', temp,'°C')\n",
        "#print('Wind:', wind)\n",
        "#print('Pressure:', pressure)\n",
        "#print('Humidity:',humidity)\n",
        "#print('Description:',description)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FfTaYoi7bbkl",
        "outputId": "36afb637-2f6a-4c32-9a6a-84634cf905cd"
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter City:Lille\n",
            "{'coord': {'lon': 3.0586, 'lat': 50.633}, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}], 'base': 'stations', 'main': {'temp': 276.57, 'feels_like': 272.44, 'temp_min': 274.22, 'temp_max': 278.54, 'pressure': 1012, 'humidity': 69}, 'visibility': 10000, 'wind': {'speed': 5.14, 'deg': 20}, 'clouds': {'all': 20}, 'dt': 1701167520, 'sys': {'type': 2, 'id': 2080387, 'country': 'FR', 'sunrise': 1701156156, 'sunset': 1701186538}, 'timezone': 3600, 'id': 2998324, 'name': 'Lille', 'cod': 200}\n",
            "Temperature: 276.57 °C\n",
            "Wind: 5.14\n",
            "Pressure: 1012\n",
            "Humidity: 69\n",
            "Description: few clouds\n"
          ]
        }
      ]
    }
  ]
}

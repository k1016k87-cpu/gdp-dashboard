{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNONc3e2chqt2nvMriyuymW",
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
        "<a href=\"https://colab.research.google.com/github/k1016k87-cpu/gdp-dashboard/blob/main/Untitled0.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from datetime import datetime, timedelta\n",
        "import pandas as pd\n",
        "from IPython.display import display\n",
        "\n",
        "\n",
        "def calculate_evaluation_table():\n",
        "    print(\"=== 病人評估期限計算系統 (表格版) ===\")\n",
        "\n",
        "    all_patient_data = [] # List to store all patient records\n",
        "\n",
        "    while True:\n",
        "        # 1. 輸入病人基本資料\n",
        "        patient_name = input(\"請輸入病人姓名: \").strip()\n",
        "        chart_number = input(\"請輸入病歷號: \").strip()\n",
        "\n",
        "        # 2. 輸入入院日期並進行格式檢查\n",
        "        while True:\n",
        "            admission_date_str = input(\n",
        "                \"請輸入入院日期 (格式 YYYY-MM-DD，例如 2026-07-01): \"\n",
        "            ).strip()\n",
        "            try:\n",
        "                admission_date = datetime.strptime(admission_date_str, \"%Y-%m-%d\")\n",
        "                break\n",
        "            except ValueError:\n",
        "                print(\"❌ 日期格式錯誤，請確保符合 YYYY-MM-DD 的格式。\")\n",
        "\n",
        "        # 3. 計算兩週後（14天）的評估表單完成日\n",
        "        deadline_date = admission_date + timedelta(days=14)\n",
        "\n",
        "        # Create a dictionary for the current patient's data\n",
        "        current_patient_record = {\n",
        "            \"病歷號碼\": chart_number,\n",
        "            \"病人姓名\": patient_name,\n",
        "            \"入院日期\": admission_date.strftime(\"%Y-%m-%d\"),\n",
        "            \"🚨 評估表單完成截止日 (兩週後)\": deadline_date.strftime(\"%Y-%m-%d\")\n",
        "        }\n",
        "        all_patient_data.append(current_patient_record)\n",
        "\n",
        "        # Ask if the user wants to add more patients\n",
        "        continue_input = input(\"是否繼續輸入下一位病人資料？ (Y/N): \").strip().lower()\n",
        "        if continue_input != 'y':\n",
        "            break\n",
        "\n",
        "    # 5. 轉換成 pandas 的 DataFrame (資料表)\n",
        "    df = pd.DataFrame(all_patient_data)\n",
        "\n",
        "    # 6. 顯示結果\n",
        "    print(\"\\n\" + \"=\" * 40)\n",
        "    print(\"        📋 病人評估排程結果\")\n",
        "    print(\"=\" * 40)\n",
        "\n",
        "    # 使用 Colab 內建的自適應網頁表格呈現\n",
        "    display(df)\n",
        "\n",
        "    # Export to CSV\n",
        "    csv_filename = \"patient_evaluation_data.csv\"\n",
        "    df.to_csv(csv_filename, index=False, encoding='utf-8-sig')\n",
        "    print(f\"\\n資料已匯出至 {csv_filename}\")\n",
        "\n",
        "\n",
        "# 執行程式\n",
        "if __name__ == \"__main__\":\n",
        "    calculate_evaluation_table()\n",
        ""
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "t_lZko1DuiTW",
        "outputId": "c9074db2-7c1f-4ae7-ec86-f1635ab17e84"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "=== 病人評估期限計算系統 (表格版) ===\n"
          ]
        }
      ]
    }
  ]
}
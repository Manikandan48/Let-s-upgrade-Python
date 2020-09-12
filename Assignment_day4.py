{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Assignment_day4.py",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyO1qrC0guJncKaglRho2Kl8",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
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
        "<a href=\"https://colab.research.google.com/github/Manikandan48/Let-s-upgrade-Python/blob/master/Assignment_day4.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "bWgSBOiY4V92",
        "colab_type": "text"
      },
      "source": [
        "1.armstrong"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5c5eTmWlkL4N",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "for i in range(1042000,702648265):  \n",
        "   sum1 = 0  \n",
        "   temp = i  \n",
        "   while temp > 0:  \n",
        "       digit = temp % 10  \n",
        "       sum1 += digit ** 3\n",
        "       temp //= 10  \n",
        "   if i== sum1:  \n",
        "     print(i)  \n",
        "     break"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}
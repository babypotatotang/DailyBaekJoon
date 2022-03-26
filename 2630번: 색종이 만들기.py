{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled4.ipynb",
      "private_outputs": true,
      "provenance": [],
      "authorship_tag": "ABX9TyP5Pc7mAzCKBTEYA3DkisNV",
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
        "<a href=\"https://colab.research.google.com/github/babypotatotang/BaekJoonMaster/blob/main/2630%EB%B2%88%3A%20%EC%83%89%EC%A2%85%EC%9D%B4%20%EB%A7%8C%EB%93%A4%EA%B8%B0.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "HiV2szJtOEf6"
      },
      "outputs": [],
      "source": [
        "#2630번: 색종이 만들기\n",
        "result=[]\n",
        "\n",
        "def Quad(dots,size,x,y):\n",
        "    dots=dots; tmpdots=[]; global result\n",
        "\n",
        "    for i in range(int(size)):\n",
        "        tmpdots.append(dots[x+i][y:y+size])\n",
        "\n",
        "    tt=sum(tmpdots,[])\n",
        "\n",
        "    if size==1:\n",
        "        for i in tt: result.append(i)\n",
        "        return 0\n",
        "\n",
        "    if tt.count(0)==size**2: return result.append(0)\n",
        "    elif tt.count(1)==size**2: return result.append(1)\n",
        "    else:\n",
        "        Quad(tmpdots,size//2,0,0)\n",
        "        Quad(tmpdots,size//2,0,size//2)\n",
        "        Quad(tmpdots,size//2,size//2,0)\n",
        "        Quad(tmpdots,size//2,size//2,size//2)\n",
        "\n",
        "size=int(input())\n",
        "dots = [list(map(int,(input().split()))) for _ in range(size)]\n",
        "\n",
        "Quad(dots,size,0,0)\n",
        "\n",
        "print(result.count(0))\n",
        "print(result.count(1))"
      ]
    }
  ]
}
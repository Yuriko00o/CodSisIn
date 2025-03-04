{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "84afa4db-7b68-463e-95f2-c21c12d8d3c4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "dime un número 45\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2.2222222222222223\n"
     ]
    }
   ],
   "source": [
    "n = input(\"dime un número\"  )\n",
    "try:\n",
    "     print(100/n)\n",
    "except:\n",
    "     print(100/int(n))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "2a2ccd83-e05d-439a-876b-5db27ae16212",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Please enter a number:  hyftdv\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Número inválido\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Please enter a number:  \n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Número inválido\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Please enter a number:  54\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Número válido\n"
     ]
    }
   ],
   "source": [
    "while True:\n",
    "    try:\n",
    "        x = int(input(\"Please enter a number: \"))\n",
    "        print(\"Número válido\")\n",
    "        break\n",
    "    except ValueError:\n",
    "        print(\"Número inválido\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9f3a61ed-6da9-4cbd-be4a-afb85eaca424",
   "metadata": {},
   "outputs": [],
   "source": [
    "import sys\n",
    "\n",
    "try:\n",
    "    f = open('myfile.txt')\n",
    "    s = f.readline()\n",
    "    i = int(s.strip())\n",
    "except OSError as err:\n",
    "    print(\"OS error:\", err)\n",
    "except ValueError:\n",
    "    print(\"Could not convert data to an integer.\")\n",
    "except Exception as err:\n",
    "    print(f\"Unexpected {err=}, {type(err)=}\")\n",
    "    raise"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1801219a-c90a-4e7c-aaf5-3e9cf0030ad4",
   "metadata": {},
   "outputs": [],
   "source": [
    "for arg in sys.argv[1:]:\n",
    "    try:\n",
    "        f = open(arg, 'r')\n",
    "    except OSError:\n",
    "        print('cannot open', arg)\n",
    "    else:\n",
    "        print(arg, 'has', len(f.readlines()), 'lines')\n",
    "        f.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6cc9de22-c084-4c43-b8f8-dde38ad785e8",
   "metadata": {},
   "outputs": [],
   "source": [
    "def this_fails():\n",
    "    x = 1/0\n",
    "\n",
    "try:\n",
    "    this_fails()\n",
    "except ZeroDivisionError as err:\n",
    "    print('Handling run-time error:', err)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7726b04a-e1f1-4372-8bdf-72ddef22f327",
   "metadata": {},
   "outputs": [],
   "source": [
    "raise NameError('HiThere')\n",
    "Traceback (most recent call last):\n",
    "  File \"<stdin>\", line 1, in <module>\n",
    "    raise NameError('HiThere')\n",
    "NameError: HiThere"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "65ae1e28-269d-41b8-8b58-1e982cf651e7",
   "metadata": {},
   "outputs": [],
   "source": [
    "try:\n",
    "    open(\"database.sqlite\")\n",
    "except OSError:\n",
    "    raise RuntimeError(\"unable to handle error\")\n",
    "\n",
    "Traceback (most recent call last):\n",
    "  File \"<stdin>\", line 2, in <module>\n",
    "    open(\"database.sqlite\")\n",
    "    ~~~~^^^^^^^^^^^^^^^^^^^\n",
    "FileNotFoundError: [Errno 2] No such file or directory: 'database.sqlite'\n",
    "\n",
    "During handling of the above exception, another exception occurred:\n",
    "\n",
    "Traceback (most recent call last):\n",
    "  File \"<stdin>\", line 4, in <module>\n",
    "    raise RuntimeError(\"unable to handle error\")\n",
    "RuntimeError: unable to handle error"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dbbf943e-37a8-445b-8991-604d42301a58",
   "metadata": {},
   "outputs": [],
   "source": [
    "def func():\n",
    "    raise ConnectionError\n",
    "\n",
    "try:\n",
    "    func()\n",
    "except ConnectionError as exc:\n",
    "    raise RuntimeError('Failed to open database') from exc\n",
    "\n",
    "Traceback (most recent call last):\n",
    "  File \"<stdin>\", line 2, in <module>\n",
    "    func()\n",
    "    ~~~~^^\n",
    "  File \"<stdin>\", line 2, in func\n",
    "ConnectionError\n",
    "\n",
    "The above exception was the direct cause of the following exception:\n",
    "\n",
    "Traceback (most recent call last):\n",
    "  File \"<stdin>\", line 4, in <module>\n",
    "    raise RuntimeError('Failed to open database') from exc\n",
    "RuntimeError: Failed to open database"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "7840c19b-6bfd-4925-97fd-a3c48166ab40",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (13551363.py, line 13)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[44], line 13\u001b[1;36m\u001b[0m\n\u001b[1;33m    executing finally\u001b[0m\n\u001b[1;37m              ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "def divide(x, y):\n",
    "    try:\n",
    "        result = x / y\n",
    "    except ZeroDivisionError:\n",
    "        print(\"division by zero!\")\n",
    "    else:\n",
    "        print(\"result is\", result)\n",
    "    finally:\n",
    "        print(\"executing finally clause\")\n",
    "\n",
    "divide(2, 1)\n",
    "result is 2.0\n",
    "executing finally clause:\n",
    "divide(2, 0)\n",
    "division by zero!\n",
    "executing finally clause:\n",
    "divide(\"2\", \"1\")\n",
    "executing finally clause:\n",
    "Traceback (most recent call last):\n",
    "  File \"<stdin>\", line 1, in <module>\n",
    "    divide(\"2\", \"1\")\n",
    "    ~~~~~~^^^^^^^^^^\n",
    "  File \"<stdin>\", line 3, in divide\n",
    "    result = x / y\n",
    "             ~~^~~\n",
    "TypeError: unsupported operand type(s) for /: 'str' and 'str'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "493435d6-f621-4d4b-ae5c-58ec33321bf8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def bool_return():\n",
    "    try:\n",
    "        return True\n",
    "    finally:\n",
    "        return False\n",
    "\n",
    "bool_return()\n",
    "False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3fdd2682-7f83-4887-892f-f873ee119213",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}


unit = ["zero","um", "dois", "três", "quatro", "cinco", "seis", "sete",
"oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze",
"dezesseis", "dezessete", "dezoito", "dezenove"]

dozen = ["", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta",
"setenta", "oitenta", "noventa"]

hundred = ["", "cento", "duzentos", "trezentos", "quatrocentos", "quinhentos",
"seiscentos", "setecentos", "oitocentos", "novecentos"]

word = ["", "mil"]


def _get_conjunction_and_remove_first_zero(written_number):
	to_be_removed = "zero"
	conjunction = " e "

	if (to_be_removed in written_number) or (written_number == "") or \
	(written_number.startswith(conjunction)):
		written_number = written_number.replace(to_be_removed, "")
		return "", written_number

	return " e ", written_number

def _get_unit_str_and_update_number(number, current_digit):
	dozen = number % 100

	if (dozen >= 10) and (dozen <= 19):
		return unit[dozen], int(number/100), 2

	return unit[current_digit], int(number/10), 1

def _write_hundred(number, written_number, digit_count):
	digit_count += 1
	current_digit = number % 10
	mod_1000 = number%1000

	if (digit_count == 1):
		if (mod_1000 == 100):
			return int(number/1000), "cem"
		elif(mod_1000 == 0):
			return int(number/1000), ""
		else:
			unit_str, number, digit_count= _get_unit_str_and_update_number(number, current_digit)
			written_number = written_number + unit_str
	else:
		number = int(number/10)
		conjunction, written_number = _get_conjunction_and_remove_first_zero(written_number)
		if (digit_count == 2):
			written_number = dozen[current_digit] + conjunction + written_number
		elif (digit_count == 3):
			written_number = hundred[current_digit] + conjunction + written_number
			return number, written_number
	
	if (number > 0):
		return _write_hundred(number, written_number, digit_count)
	else:
	 	return number, written_number

def _write_thousand_and_more(number, written_number, number_first_part, count):
	conjunction,_ = _get_conjunction_and_remove_first_zero(written_number)
	number_word = word[count]
	
	number_first_part_word = "" if (number_first_part == "") else \
	number_first_part + " " + number_word

	written_number = number_first_part_word + conjunction + written_number

	return number, written_number

def _write_number(number, written_number, count):
	count+=1
	number = abs(number)

	number, written_number_part = _write_hundred(number, "", 0)

	if (count == 1):
		written_number = written_number_part
	elif (count > 1):
		number, written_number = _write_thousand_and_more(number, written_number, \
			written_number_part, count-1)
	
	if (number > 0):
		return _write_number(number, written_number, count)

	return written_number

def write_number(number):
	written_number = _write_number(number, "", 0)

	if (number < 0):
		written_number = "menos " + written_number

	return written_number







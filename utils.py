import re


class Utils():

    def split_identifier_string(string_to_split):
        pattern = r'\d+'

        correspondence = re.findall(pattern, string_to_split)

        if correspondence:
            number = int(correspondence[0])
            return number


if __name__ == '__main__':
    print('utils')
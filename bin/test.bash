#!/bin/bash
sed "s/02/03/" teset.py | sudo tee teset.py #внесение изменений в файл name в формате "(номер строчки)s/(что меняем)01/(на что меняем)02"|сохранение этих измений
sudo rm -r test.bash
exit 0
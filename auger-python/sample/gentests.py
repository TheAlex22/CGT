import sys
sys.path.append("..")
#sys.settrace(None)
import auger
import animal, pet
import foo
import properties
import functions

#test_subjects = [animal, pet, foo.Foo, properties.Language, functions]
test_subjects = [functions]

mock_sustitutes = {
    "genericpath": "os.path",
    "genericpath": "os.path",
}

extra_imports = [
    ('random', 'Random'),
]

with auger.magic(test_subjects, mock_substitutes=mock_sustitutes, extra_imports=extra_imports):
    #main.main()
    animal.main()
    foo.main()
    properties.main()
    functions.main()

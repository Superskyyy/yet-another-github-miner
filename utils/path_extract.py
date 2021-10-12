import re


"""
pattern = re.compile(r'blob/\b[0-9a-f]{40}\b/')
a = 'https://github.com/udacity/nd0821-c2-build-model-workflow-exercises/blob/610d78a4a5dc956d1d8a92cbe44d8668740ad3a2/lesson-3-data-validation/exercises/exercise_9/starter/MLproject'
result = re.sub(pattern, '', a)
print('/'.join(result.split('/')[5:]))
"""
import numpy as np
# alias


print(np.__version__)
a = np.array([1,2,3])

print(a)

msg = "Roll a dice"

print(msg)


# np linspace

## Basic Usage:
## Generate 5 numbers between 0 and 1.

arr1 = np.linspace(0,1,5)

print(arr1)

## Without Endpoint:
## Generate 5 numbers between 0 and 1, excluding the endpoint.

arr2 = np.linspace(0,1,5, endpoint=False)

print(arr2)

## Return Step Size:
## Generate 5 numbers between 0 and 10 and also return the step size.

arr3 = np.linspace(0,10,5,retstep=True)
print(arr3)

## Negative Range:
## Generate 5 numbers between -5 and 0.

arr4 = np.linspace(-5,0,5)
print(arr4)


## Non-integer Steps:
## Generate 7 numbers between 1.5 and 4.5.

arr5 = np.linspace(1.5, 4.5, 7)

print(arr5)
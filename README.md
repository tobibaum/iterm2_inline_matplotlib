# iterm2_inline_matplotlib
plot image right into your shell with matplotlib and iterm2

## Installation
#### requirements
```
iterm2 > 2.9
tmux > 1.9
```

#### install
```
python setup.py install
```

add the following to your ```.bashrc```
```
export MPLBACKEND="module://iterm2_display.backend_iterm2"
```

## example
```
$ ipython
In [1]: from matplotlib import pyplot as plt
In [2]: from PIL import Image
In [3]: img = Image.open('puppy.jpg')
In [4]: plt.imshow(img)
In [5]: plt.show()
```

![example](https://cloud.githubusercontent.com/assets/1063330/23767104/2b7413c6-04bc-11e7-84b2-8736bcf5394a.png)

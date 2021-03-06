import numpy as np
from vispy import app
from vispy import gloo

c = app.Canvas(keys='interactive')

vertex = """
attribute vec2 a_position;
void main (void)
{
    gl_Position = vec4(a_position, 0.0, 1.0);
}
"""

fragment = """
void main()
{
    gl_FragColor = vec4(0.0, 0.0, 0.0, 1.0);
}
"""

program = gloo.Program(vertex, fragment)

program['a_position'] = np.c_[np.linspace(-1.0, +1.0, 100), np.random.uniform(-0.5,+0.5,100)]

c.show()

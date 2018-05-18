<p align="center">
    <a href="https://vimcanvas.christophermedlin.me">
        <img src="https://github.com/christopherjmedlin/vimcanvas/raw/master/logo.png"/>
    </a>
</p>
<p align="center">
  <a href="https://travis-ci.org/christopherjmedlin/vimcanvas.christophermedlin.me">
    <img src="https://travis-ci.org/christopherjmedlin/vimcanvas.christophermedlin.me.svg?branch=master" />
  </a>
  <a href="https://coveralls.io/github/christopherjmedlin/vimcanvas">
    <img src="https://coveralls.io/repos/github/christopherjmedlin/vimcanvas/badge.svg?branch=master" />
  </a>
</p>

<div id="about">
    <h1>?????</h1>
    <b>What is vimcanvas?</b>
    <p>Vimcanvas is a website in which you can collaboratively edit colored
    ASCII art with <a href="https://www.vim.org/">Vim</a>-like controls. Websockets are used so that you can see others
    editing in real time. In the future I might add other features to make things a little more fun.
    </p>
    <b>How do I use it?</b>
    <p>In order to create a canvas, use the <i>touch</i> command. You can then edit
    that canvas using the <i>vim</i> command. To list canvases, use the <i>ls</i> command. The editor, like Vim, uses the
    <i>h</i>, <i>j</i>, <i>k</i>, and <i>l</i> keys for navigation. To change a character, first enter insert mode
    using <i>a</i> or <i>i</i>, then type the character you want to change it to. To run an editor
    command, use the <i>:</i> key. To change the color of a character, use the <i>color</i> command,
    followed by the hex code of your color. Arguments like <i>red</i> and <i>yellow</i> also work.
    Finally, to change a large grouping of characters, you can highlight by entering visual
    mode with the <i>v</i> key. In this mode, instead of using insert mode to change a character,
    simply use the <i>char</i> command. Further information regarding these commands and keys is available below.
    </p>
    <b>I created a canvas and it disappeared.</b>
    <p>Currently, canvases get deleted after the last user has disconnected. I want to one day develop
        a feature that enables users to save canvases in a database, as well as a feature that allows the exportation
        of a text file containing the contents of the canvas. The former would also require a user authentication
        system. For now, however, no such feature exists.
    </p>
    <b>Why would you waste your time making something so pointless?</b>
    <p>Because I have alot of free time.</p>
    <h1>Commands</h1>
    <h3>Terminal</h3>
    <p><i>echo &lt;text&gt;</i></p>
    <p>Prints the first argument.</p>
    <p><i>ls</i></p>
    <p>Shows all currently available canvases.</p>
    <p><i>vim &lt;canvas_name&gt;</i></p>
    <p>Brings up an editor for the specified canvas.</p>
    <p><i>touch &lt;name&gt;</i></p>
    <p>Creates a new canvas with the specified name.</p>
    <h3>Editor</h3>
    <p><i>color &lt;color&gt;</i></p>
    <p>Colors the selection with the specified CSS color value.</p>
    <p><i>char &lt;char&gt;</i></p>
    <p>Changes the selection to the specified char. Normally one would use insert mode for this, however
        such a command is necessary in visual mode.
    </p>
    <p><i>location</i></p>
    <p>Outputs the user's x and y coordinates respectively on the canvas.</p>
    <p><i>move &lt;x&gt; &lt;y&gt;</i></p>
    <p>Moves the user to the specified coordinates. In conjunction with the location command, this
        can be used to move to another person's location if you can't find them.
    </p>
    <p><i>q, wq, x</i></p>
    <p>Quits the editor.</p>
    <h1>Editor Controls</h1>
    <p><i>h, j, k, l</i></p>
    <p>Move left, down, up, and right respectively.</p>
    <p><i>SHIFT + (h, j, k, l)</i></p>
    <p>In visual mode, this will move the entire highlight space as opposed to extending or shrinking it.</p>
    <p><i>a, i</i></p>
    <p>Enter insert mode.</p>
    <p><i>escape</i></p>
    <p>Exit insert/visual mode and go back to normal mode.</p>
    <p><i>+, -</i></p>
    <p>Zoom in and out.</p> 
</div>
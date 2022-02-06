# Task 15 - Scavenger Hunt 🔪


**Answer**

1. View page source and got first part of flag ```picoCTF{t```

2. Got CSS and opened it and found second part of flag ```h4ts_4_l0```

3. JavaScript content
```js
function openTab(tabName,elmnt,color) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
	tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < tablinks.length; i++) {
	tablinks[i].style.backgroundColor = "";
    }
    document.getElementById(tabName).style.display = "block";
    if(elmnt.style != null) {
	elmnt.style.backgroundColor = color;
    }
}

window.onload = function() {
    openTab('tabintro', this, '#222');
}

// This is the clue, robots.txt comes to your mind. Google web crawlers.
/* How can I keep Google from indexing my website? */
```

4. Gone to ```robots.txt``` file and got third part of flag ```t_0f_pl4c``` and got a clue ```I think this is an apache server... can you Access the next flag?``` 

5. This means that next part of flag is hidden inside apache2 server.

6. The ```.htacess``` file manages ```Apache server permissions```

7. Gone to that file and found this, the fourth part of the flag ``` 3s_2_lO0k``` and a clue ```I love making websites on my Mac, I can Store a lot of information there.```

8.  In Macs, a ```.DS_Store``` file ```stores the configurations for how the desktop looks```

9. Found the last part of the flag ```_74cceb07}```

In total the flag is :-
```picoCTF{th4ts_4_l0t_0f_pl4c3s_2_lO0k_74cceb07}```
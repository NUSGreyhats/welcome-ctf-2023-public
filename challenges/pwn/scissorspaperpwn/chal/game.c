#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

/* gcc -g -static -no-pie -o game game.c */

#define FLAG "greyhats{Game_hacker_in_the_making?}\n"

int generateAIChoice(int playerChoice) {
    printf("\n");
    switch (playerChoice) {
        case 0:
            printf("You chose Scissors.\n");
            printf("AI chose Stone.\n");
            return 2;
        case 1:
            printf("You chose Paper.\n");
            printf("AI chose Scissors.\n");
            return 0;
        case 2:
            printf("You chose Stone.\n");
            printf("AI chose Paper.\n");
            return 1;
        default:
            printf("Invalid choice %d.\n\n", playerChoice);
            return -1;
    }
}

int getResult(int playerChoice, int aiChoice) {
    if (aiChoice == playerChoice) {
        return 0;
    } else if ((aiChoice == 0 && playerChoice == 1) ||
               (aiChoice == 1 && playerChoice == 2) ||
               (aiChoice == 2 && playerChoice == 0)) {
        return -1;
    } else {
        return 1;
    }
}

char buf[32];
int score = 0, result;
int playerChoice, aiChoice;

void init();
int main() {
    init();

    while (score < 10) {
        printf("Current score: %d\n", score);
        printf("Choose:\n");
        printf("0: Scissors\n");
        printf("1: Paper\n");
        printf("2: Stone\n");

        memset(buf, 0, 32);
        printf("Your choice: ");
        gets(buf);
        playerChoice = atoi(buf);
        aiChoice = generateAIChoice(playerChoice);

        if (aiChoice < 0) {
            continue;
        }

        result = getResult(playerChoice, aiChoice);
        switch (result) {
            case 0: // Draw
                printf("Draw!\n\n");
                break;
            case 1: // Win
                printf("You win! How??\n\n");
                score++;
                break;
            case -1: // Lose
                printf("You lose! Ha >:)\n\n");
                break;
        }
    }

    printf("You win! How did you even %d points?!?\n", score);
    printf("As promised, here is the flag:\n");
    printf(FLAG);

    return 0;
}

void init() {
    // Time limit
    alarm(60);

    // Disable buffering on stdin and stdout
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);

    // Print banner
    printf("  _________      .__                                 __________                           __________                \n");
    printf(" /   _____/ ____ |__| ______ _________________  _____\\______   \\_____  ______   __________\\______   \\__  _  ______  \n");
    printf(" \\_____  \\_/ ___\\|  |/  ___//  ___/  _ \\_  __ \\/  ___/|     ___/\\__  \\ \\____ \\_/ __ \\_  __ \\     ___/\\ \\/ \\/ /    \\ \n");
    printf(" /        \\  \\___|  |\\___ \\ \\___ (  <_> )  | \\/\\___ \\ |    |     / __ \\|  |_> >  ___/|  | \\/    |     \\     /   |  \\\n");
    printf("/_______  /\\___  >__/____  >____  >____/|__|  /____  >|____|    (____  /   __/ \\___  >__|  |____|      \\/\\_/|___|  /\n");
    printf("        \\/     \\/        \\/     \\/                 \\/                \\/|__|        \\/                            \\/ \n\n");

    printf("Welcome to ScissorsPaperPwn!\n");
    printf("Win 10 times to get the flag!\n\n");
}

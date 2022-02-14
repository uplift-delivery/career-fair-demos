import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class BowlingGameTest {

    BowlingGame game = new BowlingGame();

    public void RollMany(int pins, int rolls) {
        for (int i = 0; i < rolls; ++i) {
            game.roll(pins);
        }
    }

    @Test
    public void WhenAllRollsAreGutterBallsThenScoreIsZero() {

        RollMany(0, 20);
        assertEquals(0, game.score());
    }

    @Test
    public void WhenAllRollsAreSinglePinsThenScoreIsTwenty() {

        RollMany(1, 20);
        assertEquals(20, game.score());
    }

    @Test
    public void WhenRollingASpareThenScoreIsTenPlusTheNextRoll() {

        game.roll(7);
        game.roll(3);
        game.roll(3);
        RollMany(0, 17);

        assertEquals(16, game.score());
    }

    @Test
    public void WhenRollingAStrikeThenScoreIsTenPlusNextTwoRolls() {

        game.roll(10);
        game.roll(3);
        game.roll(3);
        RollMany(0, 16);

        assertEquals(22, game.score());
    }

    @Test
    public void WhenRollingALlStrikesThenScoreIs300() {

        RollMany(10, 12);

        assertEquals(300, game.score());
    }

}
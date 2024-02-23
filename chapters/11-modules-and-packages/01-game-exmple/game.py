import draw
import logic

def main():
    result = logic.play_game()
    draw.draw_game(result)

if __name__ == '__main__':
    main()

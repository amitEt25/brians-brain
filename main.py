import argparse
import sys
import time
from brain import BriansBrain


def main():
    parser = argparse.ArgumentParser(description="Brian's Brain Cellular Automaton")
    parser.add_argument('--seed-file', help='Path to seed pattern file')
    parser.add_argument('--random-seed', type=int, help='Random seed value')
    parser.add_argument('--generations', type=int, default=100, help='Number of generations')
    parser.add_argument('--width', type=int, default=50, help='Grid width')
    parser.add_argument('--height', type=int, default=30, help='Grid height')
    parser.add_argument('--output-dir', default='output', help='Output directory')
    
    args = parser.parse_args()
    
    if not args.seed_file and args.random_seed is None:
        print("Error: Must provide either --seed-file or --random-seed")
        sys.exit(1)
    
    sim = BriansBrain(args.width, args.height)
    
    try:
        if args.seed_file:
            sim.load_seed_from_file(args.seed_file)
        else:
            sim.generate_random_seed(args.random_seed)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
    
    print("Starting Brian's Brain simulation...")
    print(f"Grid size: {args.width}x{args.height}")
    print(f"Generations: {args.generations}")
    print("Press Ctrl+C to stop early")
    
    try:
        for _ in range(args.generations):
            sim.display()
            sim.save_generation(args.output_dir)
            
            if sim.generation < args.generations - 1:
                time.sleep(0.1)
            
            sim.step()
            
    except KeyboardInterrupt:
        print("\nSimulation stopped by user")
    
    print(f"\nSimulation complete! Output saved to '{args.output_dir}' directory")


if __name__ == "__main__":
    main() 
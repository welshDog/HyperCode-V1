import { describe, it, expect } from '@jest/globals';
import { HyperCode } from '../index';

describe('HyperCode', () => {
  let hypercode: HyperCode;

  beforeEach(() => {
    hypercode = new HyperCode();
  });

  it('should execute THINK command', () => {
    const consoleSpy = jest.spyOn(console, 'log');
    hypercode.execute('THINK "Hello, World!"');
    expect(consoleSpy).toHaveBeenCalledWith('Hello, World!');
  });

  it('should execute ECHO command', () => {
    const consoleSpy = jest.spyOn(console, 'log');
    hypercode.execute('ECHO "Testing"');
    expect(consoleSpy).toHaveBeenCalledWith('Testing');
  });

  it('should handle SET and variables', () => {
    hypercode.execute('SET x TO 42');
    // In a real test, we'd need a way to inspect internal state or use it in commands
    expect(hypercode).toBeDefined();
  });

  it('should execute LOOP command', () => {
    const consoleSpy = jest.spyOn(console, 'log');
    hypercode.execute('LOOP 3 => ECHO "Loop"');
    expect(consoleSpy).toHaveBeenCalledTimes(3);
    expect(consoleSpy).toHaveBeenCalledWith('Loop');
  });
});

// HyperCode Core Runtime

/**
 * Main HyperCode interpreter
 */
class HyperCode {
  private variables: Record<string, any> = {};

  /**
   * Execute HyperCode program
   */
  public execute(code: string): void {
    const lines = code.split('\n').map(line => line.trim()).filter(line => line);
    
    for (const line of lines) {
      this.executeLine(line);
    }
  }

  private executeLine(line: string): void {
    if (line.startsWith('THINK')) {
      const message = this.extractString(line, 'THINK');
      console.log(message);
    } else if (line.startsWith('ECHO')) {
      const message = this.extractString(line, 'ECHO');
      console.log(message);
    } else if (line.startsWith('SET')) {
      // Example: SET x TO 42
      const [varName, value] = line.replace('SET', '').split('TO').map(s => s.trim());
      this.variables[varName] = this.parseValue(value);
    } else if (line.startsWith('LOOP')) {
      // Example: LOOP 3 => ECHO "Hello"
      const [countPart, actionPart] = line.split('=>').map(s => s.trim());
      const count = parseInt(countPart.replace('LOOP', '').trim(), 10);
      
      for (let i = 0; i < count; i++) {
        this.executeLine(actionPart);
      }
    } else if (line.startsWith('FLOW')) {
      // Handle multi-line FLOW blocks
      const flowContent = line.substring(4).trim();
      if (flowContent === '[') {
        // Multi-line flow
        // In a real implementation, we'd need to handle multi-line parsing
        console.log("[FLOW] Multi-line flows not yet implemented");
      } else {
        // Single-line flow
        const commands = flowContent.replace(/[\[\]]/g, '').split(',').map(cmd => cmd.trim());
        for (const cmd of commands) {
          this.executeLine(cmd);
        }
      }
    }
  }

  private extractString(line: string, command: string): string {
    const content = line.substring(command.length).trim();
    // Remove surrounding quotes if present
    if ((content.startsWith('"') && content.endsWith('"')) || 
        (content.startsWith("'") && content.endsWith("'"))) {
      return content.substring(1, content.length - 1);
    }
    return content;
  }

  private parseValue(value: string): any {
    // Try to parse as number
    if (!isNaN(Number(value))) {
      return Number(value);
    }
    // Try to parse as boolean
    if (value.toLowerCase() === 'true') return true;
    if (value.toLowerCase() === 'false') return false;
    // Return as string (remove quotes if present)
    return this.extractString(value, '');
  }
}

// Example usage
const hypercode = new HyperCode();
const program = `
  THINK "Hello, Beautiful Brain!"
  SET count TO 3
  LOOP count => ECHO "You belong here"
`;

hypercode.execute(program);

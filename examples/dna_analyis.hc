# dna_analysis.hc
# Advanced DNA Sequence Analysis with HyperCode

# === DNA Sequence Type ===
type DNA = string with {
  # Basic properties
  length: () → number
  gc_content: () → number
  molecular_weight: () → number
  
  # Transformations
  complement: () → DNA
  reverse_complement: () → DNA
  transcribe: () → RNA
  translate: (table=1) → Protein
  
  # Analysis
  find_motifs: (motif: string) → [number]
  find_restriction_sites: () → {enzyme: string, position: number, sequence: string}[]
  calculate_melting_temp: () → number
  
  # File I/O
  to_fasta: (header="sequence") → string
  save_to_file: (filename: string) → void
}

# === Example: CRISPR Target Finder ===
find_crispr_targets = { sequence: DNA, pam="NGG" → 
  # Find all PAM sites
  pam_sites = sequence.find_motifs(pam)
  
  # Get 20bp upstream of each PAM as potential target
  targets = pam_sites | map { pos → 
    start = max(0, pos - 23)
    end = pos
    {
      position: pos,
      sequence: sequence.slice(start, end),
      gc: sequence.slice(start, end).gc_content(),
      score: calculate_off_target_score(sequence, start, end)
    }
  }
  
  # Filter and sort
  targets
    | filter { 0.4 <= _.gc <= 0.8 }  # Optimal GC content
    | sort { -_.score }              # Sort by specificity
}

# === DNA Assembly Simulation ===
assemble_genome = { reads: [DNA], min_overlap=20 → 
  # Simple greedy assembly
  assembly = reads[0]
  remaining_reads = reads[1..]
  
  while remaining_reads.length > 0 {
    best = remaining_reads | map_with_index { read, i → 
      {overlap, pos} = find_best_overlap(assembly, read, min_overlap)
      {read, i, overlap, pos}
    } | max { _.overlap }
    
    if best.overlap < min_overlap {
      throw "Assembly failed: insufficient overlap"
    }
    
    assembly = merge_sequences(assembly, best.read, best.pos)
    remaining_reads.splice(best.i, 1)
  }
  
  assembly
}

# === Example Usage ===
# Load a genome
genome = load_fasta("genome.fasta") as DNA

# Find CRISPR targets
targets = genome 
  | find_crispr_targets("NGG")
  | take(5)  # Get top 5 targets

# Analyze each target
results = targets | map { target → 
  # Check for off-targets
  off_targets = genome.find_off_targets(target.sequence)
  
  # Return analysis
  {
    target: target.sequence,
    position: target.position,
    gc: target.gc,
    off_targets: off_targets.length,
    risk: off_targets.length > 0 ? "High" : "Low"
  }
}

# Generate report
report = {
  `# CRISPR Target Analysis Report
  ## Genome: ${genome.to_fasta().split("\n")[0]}
  ## Total Targets Found: ${targets.length}
  
  ## Top 5 Targets:
  ${results | enumerate | map { i, t → 
    `### Target ${i+1}
    - **Sequence**: ${t.target}
    - **Position**: ${t.position}
    - **GC Content**: ${(t.gc * 100).toFixed(1)}%
    - **Off-Targets**: ${t.off_targets}
    - **Risk**: ${t.risk}
  `} | join("\n\n")}
  `
}

# Save results
report.save_to_file("crispr_analysis.md")
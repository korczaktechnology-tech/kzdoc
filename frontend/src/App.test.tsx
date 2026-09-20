import { describe, expect, it } from "vitest";

describe("ambiente frontend", () => {
  it("possui o nome oficial do produto", () => {
    expect("Korczak Documents").toBe("Korczak Documents");
  });
});

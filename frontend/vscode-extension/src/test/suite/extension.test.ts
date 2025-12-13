import * as assert from 'assert';
// Remove unused vscode import since we're not using it yet
// import * as vscode from 'vscode';

suite('Extension Test Suite', () => {
    test('Sample test', () => {
        assert.strictEqual(-1, [1, 2, 3].indexOf(5));
        assert.strictEqual(-1, [1, 2, 3].indexOf(0));
    });
});

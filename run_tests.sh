#!/bin/bash

echo "======================================"
echo "Running Network Enumeration Tool Tests"
echo "======================================"
echo ""

# Test 1: Help
echo "[TEST 1] Checking --help..."
python main.py --help > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "✅ Help works"
else
    echo "❌ Help failed"
fi
echo ""

# Test 2: Single IP
echo "[TEST 2] Testing single IP (127.0.0.1)..."
python main.py 127.0.0.1 -o test_single.md > /dev/null 2>&1
if [ -f "test_single.md" ]; then
    echo "✅ Single IP scan works"
    rm test_single.md
else
    echo "❌ Single IP scan failed"
fi
echo ""

# Test 3: Custom output
echo "[TEST 3] Testing custom output path..."
mkdir -p test_output
python main.py 127.0.0.1 -o test_output/custom.md > /dev/null 2>&1
if [ -f "test_output/custom.md" ]; then
    echo "✅ Custom output works"
    rm -rf test_output
else
    echo "❌ Custom output failed"
fi
echo ""

# Test 4: Check samples directory
echo "[TEST 4] Verifying sample reports..."
SAMPLE_COUNT=$(ls -1 samples/*.md 2>/dev/null | wc -l)
if [ $SAMPLE_COUNT -ge 5 ]; then
    echo "✅ Found $SAMPLE_COUNT sample reports (need 5+)"
else
    echo "⚠️  Found only $SAMPLE_COUNT sample reports (need 5+)"
fi
echo ""

echo "======================================"
echo "Testing Complete!"
echo "======================================"
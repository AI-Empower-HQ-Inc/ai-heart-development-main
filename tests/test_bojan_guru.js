import { describe, test, expect, jest } from '@jest/globals';
import BojanGuru from '../src/gurus/BojanGuru';

describe('BojanGuru', () => {
    let guru;

    beforeEach(() => {
        guru = new BojanGuru();
        global.fetch = jest.fn();
    });

    test('should have correct initialization properties', () => {
        expect(guru.name).toBe('🌟 AI Bojan Guru');
        expect(guru.specialization).toBe('Transformative spiritual coaching and self-realization');
        expect(guru.basePrompt).toContain('You are AI Bojan Guru');
    });

    test('should return core teachings', () => {
        const teachings = guru.getTeachings();
        expect(teachings).toHaveLength(5);
        expect(teachings).toContain('Direct realization of your true nature');
        expect(teachings).toContain('Integration of spiritual wisdom in daily life');
    });

    test('should handle successful API response', async () => {
        const mockResponse = {
            success: true,
            message: 'Test response'
        };

        global.fetch.mockImplementationOnce(() =>
            Promise.resolve({
                json: () => Promise.resolve(mockResponse)
            })
        );

        const response = await guru.getResponse('What is true nature?');
        expect(response).toEqual(mockResponse);
    });

    test('should handle API errors gracefully', async () => {
        global.fetch.mockImplementationOnce(() =>
            Promise.reject(new Error('API Error'))
        );

        const response = await guru.getResponse('Test question');
        expect(response.error).toContain('Unable to connect with Bojan Guru');
    });
});
